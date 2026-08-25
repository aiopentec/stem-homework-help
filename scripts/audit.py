"""
STEM Answered — repo health check.

Runs structural checks on the Jekyll source tree that would otherwise only
surface as silent breakage on the live site (missing layouts, malformed
front matter, orphaned collection pages, duplicate post slugs).

Exits non-zero if any CRITICAL issue is found, so the GitHub Actions run
fails loudly instead of reporting green on a broken repo.
"""

import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
LAYOUTS_DIR = ROOT / "_layouts"
POSTS_DIR = ROOT / "_posts"
TOPICS_DIR = ROOT / "_topics"
CONCEPTS_DIR = ROOT / "_concepts"

VALID_SUBJECTS = {"math", "physics", "chemistry", "stats"}

issues = []  # list of (severity, message)


def flag(severity, message):
    issues.append((severity, message))


def split_front_matter(text, path):
    """Return (front_matter_dict, body) or (None, None) if malformed."""
    if not text.startswith("---\n"):
        flag("CRITICAL", f"{path.name}: missing front matter delimiter")
        return None, None

    parts = text.split("---\n", 2)
    if len(parts) < 3:
        flag("CRITICAL", f"{path.name}: unterminated front matter block")
        return None, None

    try:
        front_matter = yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError as e:
        flag("CRITICAL", f"{path.name}: front matter is not valid YAML ({e})")
        return None, None

    return front_matter, parts[2]


def check_layouts_exist():
    """Every layout referenced anywhere in the repo must exist in _layouts/."""
    available = {p.stem for p in LAYOUTS_DIR.glob("*.html")} if LAYOUTS_DIR.exists() else set()

    for collection_dir in (POSTS_DIR, TOPICS_DIR, CONCEPTS_DIR):
        if not collection_dir.exists():
            continue
        for path in collection_dir.glob("*.md"):
            fm, _ = split_front_matter(path.read_text(encoding="utf-8"), path)
            if fm is None:
                continue
            layout = fm.get("layout")
            if layout and layout not in available:
                flag(
                    "CRITICAL",
                    f"{path.relative_to(ROOT)}: layout '{layout}' has no "
                    f"matching file in _layouts/ (page will render with no "
                    f"header/nav/CSS)",
                )


def check_post_front_matter():
    """Every post needs the fields the templates actually depend on."""
    required = {"layout", "title", "author", "category"}
    seen_slugs = {}

    if not POSTS_DIR.exists():
        return

    for path in sorted(POSTS_DIR.glob("*.md")):
        fm, _ = split_front_matter(path.read_text(encoding="utf-8"), path)
        if fm is None:
            continue

        missing = required - fm.keys()
        if missing:
            flag(
                "CRITICAL",
                f"{path.name}: missing front matter field(s): {sorted(missing)}",
            )

        category = fm.get("category")
        if category and category not in VALID_SUBJECTS:
            flag(
                "WARNING",
                f"{path.name}: category '{category}' is not one of {sorted(VALID_SUBJECTS)}",
            )

        if not fm.get("description"):
            flag(
                "WARNING",
                f"{path.name}: no explicit 'description' front matter "
                f"(auto meta description may fall back to full body text)",
            )

        # Duplicate slug/filename check (date-site-slug should be unique).
        if path.name in seen_slugs:
            flag("CRITICAL", f"{path.name}: duplicate post filename")
        seen_slugs[path.name] = True


def check_orphaned_collection_entries():
    """
    Topics/concepts declared in _data but with no live page are silent gaps,
    not broken pages — flagged as INFO so the weekly report keeps a running
    count of the backlog without failing the build over it.
    """
    data_dir = ROOT / "_data"
    topics_yml = data_dir / "topics.yml"
    concepts_yml = data_dir / "concepts.yml"

    if topics_yml.exists():
        declared = yaml.safe_load(topics_yml.read_text(encoding="utf-8")) or {}
        declared_slugs = {
            topic["slug"]
            for subject_topics in declared.values()
            for topic in subject_topics.values()
        }
        existing_slugs = (
            {p.stem for p in TOPICS_DIR.glob("*.md")} if TOPICS_DIR.exists() else set()
        )
        missing = declared_slugs - existing_slugs
        if missing:
            flag(
                "INFO",
                f"{len(missing)} topic page(s) declared in _data/topics.yml "
                f"with no live page yet: {sorted(missing)}",
            )

    if concepts_yml.exists():
        declared = yaml.safe_load(concepts_yml.read_text(encoding="utf-8")) or {}
        existing_slugs = (
            {p.stem for p in CONCEPTS_DIR.glob("*.md")} if CONCEPTS_DIR.exists() else set()
        )
        missing = set(declared.keys()) - existing_slugs
        if missing:
            flag(
                "INFO",
                f"{len(missing)} concept page(s) declared in _data/concepts.yml "
                f"with no live page yet: {sorted(missing)}",
            )


def check_search_index_freshness():
    """data/search.json should have roughly one entry per post."""
    search_json = ROOT / "data" / "search.json"
    post_count = len(list(POSTS_DIR.glob("*.md"))) if POSTS_DIR.exists() else 0

    if not search_json.exists():
        flag("WARNING", "data/search.json does not exist")
        return

    import json

    try:
        index = json.loads(search_json.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        flag("CRITICAL", f"data/search.json is not valid JSON ({e})")
        return

    if len(index) < post_count:
        flag(
            "WARNING",
            f"data/search.json has {len(index)} entries but there are "
            f"{post_count} posts — search index is stale or was never generated",
        )


def main():
    check_layouts_exist()
    check_post_front_matter()
    check_orphaned_collection_entries()
    check_search_index_freshness()

    critical = [m for sev, m in issues if sev == "CRITICAL"]
    warning = [m for sev, m in issues if sev == "WARNING"]
    info = [m for sev, m in issues if sev == "INFO"]

    print(f"\n=== Repo health check: {len(issues)} finding(s) ===\n")

    for label, group in (("CRITICAL", critical), ("WARNING", warning), ("INFO", info)):
        if not group:
            continue
        print(f"-- {label} ({len(group)}) --")
        for m in group:
            print(f"  {m}")
        print()

    if not issues:
        print("No issues found.")

    if critical:
        print(f"FAILING: {len(critical)} critical issue(s) found.")
        sys.exit(1)

    sys.exit(0)


if __name__ == "__main__":
    main()
