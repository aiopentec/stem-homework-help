import glob
import re

FRONT_MATTER_RE = re.compile(r"^(---\n.*?\n---\n)(.*)$", re.DOTALL)

wrapped = 0
skipped = 0
no_front_matter = 0

for path in sorted(glob.glob("_posts/*.md")):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    m = FRONT_MATTER_RE.match(content)
    if not m:
        print(f"SKIP (no front matter found): {path}")
        no_front_matter += 1
        continue

    front_matter, rest = m.groups()
    body = rest.lstrip("\n")

    if body.startswith("{% raw %}"):
        print(f"SKIP (already wrapped): {path}")
        skipped += 1
        continue

    new_body = "{% raw %}\n" + body.rstrip("\n") + "\n{% endraw %}\n"
    new_content = front_matter + "\n" + new_body

    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"WRAPPED: {path}")
    wrapped += 1

print(f"\nDone. Wrapped: {wrapped}, already wrapped (skipped): {skipped}, no front matter: {no_front_matter}")
