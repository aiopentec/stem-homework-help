def calculate_quality(
    verification,
    metadata,
    solution,
    related_questions_count=0
):

    verification_score = verification.get(
        "score", 0
    )

    completeness = 100

    required_sections = [
        "Quick Answer",
        "Understanding the Problem",
        "Solution",
        "Final Answer",
        "Why This Works",
        "Key Concept",
        "Common Mistakes",
    ]

    for section in required_sections:
        if section.lower() not in solution.lower():
            completeness -= 10

    linking_score = min(
        100,
        related_questions_count * 20
    )

    score = (
        verification_score * 0.60
        + completeness * 0.25
        + linking_score * 0.15
    )

    score = round(score)

    return {
        "score": score,
        "publishable": (
            score >= 80
            and verification_score >= 80
            and not verification.get(
                "critical_error",
                True
            )
        )
    }
