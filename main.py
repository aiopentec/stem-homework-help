"""
STEM Answered V2
Main orchestration entry point.

The pipeline is intentionally conservative:
Discovery
→ Deduplication
→ Classification
→ Generation
→ Verification
→ Repair
→ Quality Gate
→ Publishing
→ Search Index
→ IndexNow
"""

import json
import os
from pathlib import Path

from scripts.discovery import get_unanswered_questions
from scripts.deduplicator import load_processed, save_processed
from scripts.classifier import classify_question
from scripts.generator import generate_solution
from scripts.verifier import verify_solution
from scripts.repair import repair_solution
from scripts.quality import calculate_quality
from scripts.linker import build_related_questions
from scripts.publisher import write_post
from scripts.indexer import build_search_index


SITE = os.environ.get("SITE", "math")

QUESTIONS_PER_RUN = int(
    os.environ.get("QUESTIONS_PER_RUN", "1")
)

MAX_REPAIR_ATTEMPTS = int(
    os.environ.get("MAX_REPAIR_ATTEMPTS", "2")
)

SITE_URL = os.environ.get(
    "SITE_URL",
    "https://stemanswered.com"
).rstrip("/")


def load_taxonomy():
    """Load topics and concepts from _data."""

    import yaml

    topics_path = Path("_data/topics.yml")
    concepts_path = Path("_data/concepts.yml")

    with open(topics_path, "r", encoding="utf-8") as f:
        topics = yaml.safe_load(f) or []

    with open(concepts_path, "r", encoding="utf-8") as f:
        concepts = yaml.safe_load(f) or []

    return topics, concepts


def load_existing_content():
    """
    Load lightweight metadata from existing posts.

    This is used for internal linking and does not modify
    existing content.
    """

    from scripts.indexer import load_content_index

    return load_content_index()


def process_question(
    question,
    topics,
    concepts,
    existing_content
):
    """Process one Stack Exchange question."""

    question_id = str(
        question["question_id"]
    )

    print(
        f"\nProcessing question {question_id}: "
        f"{question['title']}"
    )

    # ---------------------------------------------------------
    # 1. CLASSIFICATION
    # ---------------------------------------------------------

    try:
        metadata = classify_question(
            question,
            topics,
            concepts
        )
    except Exception as exc:
        print(
            f"Classification failed: {exc}"
        )
        return None

    print(
        "Classification:",
        metadata
    )

    # ---------------------------------------------------------
    # 2. GENERATION
    # ---------------------------------------------------------

    solution = generate_solution(
        question,
        metadata
    )

    if not solution:
        print("Generation failed.")
        return None

    # ---------------------------------------------------------
    # 3. VERIFICATION + REPAIR LOOP
    # ---------------------------------------------------------

    verification = verify_solution(
        question,
        solution,
        metadata
    )

    repair_attempts = 0

    while (
        not verification.get("passed", False)
        or verification.get("score", 0) < 80
    ) and repair_attempts < MAX_REPAIR_ATTEMPTS:

        repair_attempts += 1

        print(
            f"Verification failed. "
            f"Repair attempt {repair_attempts}."
        )

        repaired = repair_solution(
            question,
            solution,
            verification,
            metadata
        )

        if not repaired:
            break

        solution = repaired

        verification = verify_solution(
            question,
            solution,
            metadata
        )

    # ---------------------------------------------------------
    # 4. FINAL QUALITY GATE
    # ---------------------------------------------------------

    quality = calculate_quality(
        verification=verification,
        metadata=metadata,
        solution=solution
    )

    print(
        f"Verification score: "
        f"{verification.get('score', 0)}"
    )

    print(
        f"Quality score: "
        f"{quality['score']}"
    )

    if not quality["publishable"]:
        print(
            "QUALITY GATE FAILED. "
            "Question will not be published."
        )
        return {
            "status": "rejected",
            "question_id": question_id,
            "verification": verification,
            "quality": quality,
        }

    # ---------------------------------------------------------
    # 5. INTERNAL LINKING
    # ---------------------------------------------------------

    related_questions = build_related_questions(
        current={
            **metadata,
            "question_id": question_id,
            "title": question["title"],
        },
        existing_questions=existing_content,
        limit=6
    )

    # ---------------------------------------------------------
    # 6. PUBLISH
    # ---------------------------------------------------------

    filename, public_url = write_post(
        question=question,
        solution=solution,
        metadata=metadata,
        verification=verification,
        quality=quality,
        related_questions=related_questions
    )

    print(
        f"Published: {filename}"
    )

    return {
        "status": "published",
        "question_id": question_id,
        "filename": filename,
        "url": public_url,
        "verification": verification,
        "quality": quality,
    }


def ping_indexnow(url):
    """Notify IndexNow after successful publishing."""

    import requests

    key = os.environ.get("INDEXNOW_KEY")

    if not key:
        return

    try:
        requests.get(
            "https://api.indexnow.org/indexnow",
            params={
                "url": url,
                "key": key
            },
            timeout=10
        )

        print(
            f"IndexNow ping sent: {url}"
        )

    except Exception as exc:
        print(
            f"IndexNow ping failed "
            f"(non-fatal): {exc}"
        )


def main():

    print("=" * 60)
    print("STEM ANSWERED V2")
    print("=" * 60)

    print(f"SITE: {SITE}")
    print(
        f"QUESTIONS_PER_RUN: "
        f"{QUESTIONS_PER_RUN}"
    )

    # ---------------------------------------------------------
    # LOAD STATE
    # ---------------------------------------------------------

    processed = load_processed(SITE)

    # ---------------------------------------------------------
    # LOAD TAXONOMY
    # ---------------------------------------------------------

    topics, concepts = load_taxonomy()

    # ---------------------------------------------------------
    # LOAD CONTENT INDEX
    # ---------------------------------------------------------

    existing_content = load_existing_content()

    # ---------------------------------------------------------
    # DISCOVER QUESTIONS
    # ---------------------------------------------------------

    candidates = get_unanswered_questions(
        site=SITE,
        exclude_ids=processed,
        limit=20
    )

    if not candidates:
        print(
            "No new unanswered questions found."
        )
        return

    print(
        f"Candidates found: "
        f"{len(candidates)}"
    )

    published = []

    # ---------------------------------------------------------
    # PROCESS
    # ---------------------------------------------------------

    for question in candidates[
        :QUESTIONS_PER_RUN
    ]:

        result = process_question(
            question=question,
            topics=topics,
            concepts=concepts,
            existing_content=existing_content
        )

        if not result:
            continue

        if result["status"] == "published":

            question_id = str(
                question["question_id"]
            )

            processed.add(question_id)

            published.append(result)

    # ---------------------------------------------------------
    # SAVE STATE
    # ---------------------------------------------------------

    if published:
        save_processed(
            SITE,
            processed
        )

        for item in published:
            ping_indexnow(
                item["url"]
            )

    # ---------------------------------------------------------
    # REBUILD SEARCH INDEX
    # ---------------------------------------------------------

    print(
        "\nRebuilding search index..."
    )

    build_search_index()

    print(
        "\nSTEM Answered V2 run complete."
    )


if __name__ == "__main__":
    main()
