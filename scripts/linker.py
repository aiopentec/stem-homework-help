def build_related_questions(
    current,
    existing_questions,
    limit=6
):

    scored = []

    current_concepts = set(
        current.get("concepts", [])
    )

    for item in existing_questions:

        if item.get("url") == current.get("url"):
            continue

        score = 0

        if item.get("subject") == current.get("subject"):
            score += 30

        if item.get("topic") == current.get("topic"):
            score += 30

        item_concepts = set(
            item.get("concepts", [])
        )

        score += len(
            current_concepts & item_concepts
        ) * 15

        if item.get("difficulty") == current.get(
            "difficulty"
        ):
            score += 5

        scored.append(
            (score, item)
        )

    scored.sort(
        key=lambda x: x[0],
        reverse=True
    )

    return [
        item
        for score, item in scored[:limit]
        if score >= 30
    ]
