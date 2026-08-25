import os
import json
import time
import datetime
import re
import requests
import yaml
from google import genai
from groq import Groq

# ── Config ────────────────────────────────────────────────────────────────
SITE = os.environ.get("SITE", "math")  # math, physics, chemistry, or stats
STATE_FILE = f"processed_questions_{SITE}.json"
POSTS_DIR = "_posts"
QUESTIONS_PER_RUN = 1
GEMINI_MODEL = "gemini-flash-lite-latest"  # self-updating alias, avoids retirement breakage
GROQ_MODEL = "openai/gpt-oss-120b"

SUBJECT_LABELS = {
    "math": "mathematics",
    "physics": "physics",
    "chemistry": "chemistry",
    "stats": "statistics",
}
SE_SITE_NAMES = {
    "math": "Mathematics Stack Exchange",
    "physics": "Physics Stack Exchange",
    "chemistry": "Chemistry Stack Exchange",
    "stats": "Cross Validated (Stats Stack Exchange)",
}
SUBJECT_LABEL = SUBJECT_LABELS.get(SITE, SITE)
SE_SITE_NAME = SE_SITE_NAMES.get(SITE, "Stack Exchange")

AMAZON_TAG = "aiopentec20-20"  # Associates tracking ID

AFFILIATE_BOOKS = {
    "math": {
        "title": "Schaum's Outline of Calculus, 7th Edition",
        "asin": "126425833X",
    },
    "physics": {
        "title": "Schaum's Outline of College Physics, 12th Edition",
        "asin": "1259587398",
    },
    "chemistry": {
        "title": "Schaum's Outline of College Chemistry, 10th Edition",
        "asin": "007181082X",
    },
    "stats": {
        "title": "Schaum's Outline of Statistics, 6th Edition",
        "asin": "1260011461",
    },
}

gemini_client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
groq_client = Groq(api_key=os.environ["GROQ_API_KEY"]) if os.environ.get("GROQ_API_KEY") else None


def affiliate_link():
    book = AFFILIATE_BOOKS.get(SITE, AFFILIATE_BOOKS["math"])
    return f"https://www.amazon.com/dp/{book['asin']}?tag={AMAZON_TAG}", book["title"]


# ── State (dedupe) ───────────────────────────────────────────────────────
def load_processed():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r") as f:
            return set(json.load(f))
    return set()


def save_processed(ids):
    with open(STATE_FILE, "w") as f:
        json.dump(sorted(ids), f, indent=2)


# ── Fetch unanswered questions from Stack Exchange ──────────────────────
def get_unanswered_questions(site, exclude_ids, limit=20):
    url = "https://api.stackexchange.com/2.3/questions/unanswered"
    params = {
        "order": "desc",
        "sort": "votes",
        "site": site,
        "filter": "withbody",
        "pagesize": limit,
    }
    resp = requests.get(url, params=params, timeout=30)
    resp.raise_for_status()
    items = resp.json().get("items", [])
    candidates = [q for q in items if q["question_id"] not in exclude_ids]
    return candidates


def build_prompt(question):
    return f"""You are an expert {SUBJECT_LABEL} tutor. A student posted this problem
and never received an answer:

Title: {question['title']}
Body: {strip_html(question['body'])[:2000]}

Write a complete worked solution in Markdown:
1. Restate what's being asked in plain language
2. Show every step, don't skip any
3. State the final answer clearly
4. Add a short "Common Mistakes" section for this problem type

Do not include a closing resources section — that will be added separately."""


# ── Groq attempt (primary) ───────────────────────────────────────────────
def try_groq(prompt, max_attempts=2, max_wait=8):
    if groq_client is None:
        return None
    for attempt in range(1, max_attempts + 1):
        try:
            resp = groq_client.chat.completions.create(
                model=GROQ_MODEL,
                messages=[{"role": "user", "content": prompt}],
            )
            return resp.choices[0].message.content
        except Exception as e:
            wait = min(2 ** attempt, max_wait)
            print(f"Groq attempt {attempt} failed ({e})")
            if attempt == max_attempts:
                print("Groq exhausted, falling back to Gemini...")
                return None
            time.sleep(wait)
    return None


# ── Gemini attempt (fallback) ────────────────────────────────────────────
def try_gemini(prompt, max_attempts=2, max_wait=8):
    for attempt in range(1, max_attempts + 1):
        try:
            response = gemini_client.models.generate_content(
                model=GEMINI_MODEL,
                contents=prompt,
            )
            return response.text
        except Exception as e:
            wait = min(2 ** attempt, max_wait)
            print(f"Gemini attempt {attempt} failed ({e})")
            if attempt == max_attempts:
                print("Gemini exhausted too — skipping this question, will retry next run.")
                return None
            time.sleep(wait)
    return None


def generate_solution(question):
    prompt = build_prompt(question)
    solution = try_groq(prompt)
    if solution is None:
        solution = try_gemini(prompt)
    return solution


def strip_html(text):
    return re.sub(r"<[^>]+>", "", text or "")


def slugify(title):
    slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    return slug[:80]


# ── Build and write the Jekyll post ─────────────────────────────────────
def write_post(question, solution_body):
    date = datetime.date.today().isoformat()
    slug = slugify(question["title"])
    # Prefix with SITE so identical dates/slugs across subjects never collide.
    filename = f"{POSTS_DIR}/{date}-{SITE}-{slug}.md"

    link, book_title = affiliate_link()
    disclosure_and_link = (
        "*As an Amazon Associate, I earn from qualifying purchases.* "
        f"For more practice problems like this, see [{book_title}]({link}).\n\n"
        "---\n\n"
    )

    attribution = (
        f"\n\n*Original question: [{question['title']}]({question['link']}) "
        f"on {SE_SITE_NAME}, licensed CC BY-SA.*\n"
    )

    # yaml.safe_dump handles all escaping (backslashes, quotes, colons, LaTeX)
    # correctly, unlike manual string interpolation.
    front_matter_dict = {
        "layout": "question",
        "title": question["title"],
        "author": "StemFix Bot",
        "category": SITE,
        "subject": SITE,
        "tags": [SITE],
    }
    front_matter = "---\n" + yaml.safe_dump(
        front_matter_dict, allow_unicode=True, sort_keys=False
    ) + "---\n\n"

    # Wrap the body in {% raw %}...{% endraw %} so Jekyll's Liquid parser
    # never touches it. AI-generated LaTeX frequently produces literal "{%"
    # sequences (e.g. "\boxed{%" wrapped across a line break), which Liquid
    # otherwise misreads as an unclosed tag. render_with_liquid: false would
    # be the cleaner fix but requires Jekyll 4.0+, and GitHub Pages is
    # pinned to Jekyll 3.10 — raw/endraw works on every Liquid version.
    body = disclosure_and_link + solution_body + attribution
    content = front_matter + "{% raw %}\n" + body + "\n{% endraw %}\n"

    os.makedirs(POSTS_DIR, exist_ok=True)
    with open(filename, "w") as f:
        f.write(content)

    return filename


# ── IndexNow ping ────────────────────────────────────────────────────────
def ping_indexnow(url, key):
    try:
        requests.get(
            "https://api.indexnow.org/indexnow",
            params={"url": url, "key": key},
            timeout=10,
        )
    except Exception as e:
        print(f"IndexNow ping failed (non-fatal): {e}")


# ── Main ─────────────────────────────────────────────────────────────────
def main():
    print(f"=== Running for SITE={SITE} ===")
    processed = load_processed()
    candidates = get_unanswered_questions(SITE, processed)

    if not candidates:
        print("No new unanswered questions found.")
        return

    written = []
    for question in candidates[:QUESTIONS_PER_RUN]:
        solution = generate_solution(question)
        if solution is None:
            continue  # skip, do NOT mark as processed — retry next run
        filename = write_post(question, solution)
        written.append(filename)
        processed.add(question["question_id"])
        print(f"Wrote {filename}")

    if written:
        save_processed(processed)
        site_url = os.environ.get("SITE_URL", "").rstrip("/")
        indexnow_key = os.environ.get("INDEXNOW_KEY")
        if site_url and indexnow_key:
            for f in written:
                slug = os.path.basename(f).replace(".md", "")
                ping_indexnow(f"{site_url}/{slug}/", indexnow_key)
    else:
        print("No posts written this run.")


if __name__ == "__main__":
    main()
