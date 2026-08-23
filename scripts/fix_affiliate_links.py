import glob
import re

import yaml

AMAZON_TAG = "aiopentec20-20"

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

FRONT_MATTER_RE = re.compile(r"^---\n(.*?\n)---\n", re.DOTALL)
PLACEHOLDER_LINK_RE = re.compile(
    r"\[.*?\]\(https://www\.amazon\.com/YOUR-ASSOCIATE-TAG\)"
)

fixed = 0
skipped = 0
no_front_matter = 0
no_category = 0

for path in sorted(glob.glob("_posts/*.md")):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    if "YOUR-ASSOCIATE-TAG" not in content:
        skipped += 1
        continue

    m = FRONT_MATTER_RE.match(content)
    if not m:
        print(f"SKIP (no front matter found): {path}")
        no_front_matter += 1
        continue

    try:
        front_matter = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError as e:
        print(f"SKIP (front matter didn't parse): {path} ({e})")
        no_front_matter += 1
        continue

    category = front_matter.get("category")
    book = AFFILIATE_BOOKS.get(category)
    if book is None:
        print(f"SKIP (unrecognized/missing category '{category}'): {path}")
        no_category += 1
        continue

    link = f"https://www.amazon.com/dp/{book['asin']}?tag={AMAZON_TAG}"
    replacement = f"[{book['title']}]({link})"

    new_content, n = PLACEHOLDER_LINK_RE.subn(replacement, content)
    if n == 0:
        print(f"SKIP (placeholder text present but link pattern not matched): {path}")
        continue

    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"FIXED ({category}): {path}")
    fixed += 1

print(
    f"\nDone. Fixed: {fixed}, no placeholder present (skipped): {skipped}, "
    f"no front matter: {no_front_matter}, unrecognized category: {no_category}"
)
