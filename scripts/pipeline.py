from .discovery import get_candidates
from .deduplicator import is_duplicate
from .classifier import classify_question
from .generator import generate_solution
from .verifier import verify_solution
from .quality import calculate_quality


def run_pipeline():

    questions = get_candidates()

    for question in questions:

        if is_duplicate(question):
            continue

        metadata = classify_question(
            question,
            [],
            []
        )

        solution = generate_solution(
            question,
            metadata
        )

        verification = verify_solution(
            question,
            solution,
            metadata
        )

        if not verification["passed"]:

            print(
                "Verification failed:",
                question["question_id"]
            )

            continue

        quality = calculate_quality(
            verification,
            metadata,
            solution
        )

        if not quality["publishable"]:

            print(
                "Quality gate failed:",
                question["question_id"]
            )

            continue

        # Publication step will be added here.
