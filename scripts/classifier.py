import json
import os

from google import genai

client = genai.Client(
    api_key=os.environ["GEMINI_API_KEY"]
)

MODEL = "gemini-flash-lite-latest"


ALLOWED_SUBJECTS = {
    "math",
    "physics",
    "chemistry",
    "stats",
}


def classify_question(question, available_topics, available_concepts):

    prompt = f"""
You are the classification engine for STEM Answered.

Classify the following STEM question.

QUESTION TITLE:
{question["title"]}

QUESTION BODY:
{question["body"][:5000]}

Allowed subjects:
{json.dumps(sorted(ALLOWED_SUBJECTS))}

Available topics:
{json.dumps(available_topics)}

Available concepts:
{json.dumps(available_concepts)}

Rules:

1. Choose exactly one subject.
2. Choose exactly one topic when possible.
3. Choose 1-5 concepts.
4. Do not invent a concept when a suitable existing concept exists.
5. Estimate difficulty as beginner, intermediate, advanced, or expert.
6. Determine the question type.
7. Determine whether numerical calculation is required.
8. Return JSON only.

Allowed question types:

- calculation
- conceptual
- proof
- derivation
- explanation
- comparison
- interpretation
- troubleshooting
- theoretical
- other

Return:

{{
  "subject": "...",
  "topic": "...",
  "concepts": ["..."],
  "difficulty": "...",
  "question_type": "...",
  "requires_calculation": true
}}
"""

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt
    )

    text = response.text.strip()

    if text.startswith("```"):
        text = text.replace("```json", "")
        text = text.replace("```", "")
        text = text.strip()

    result = json.loads(text)

    if result["subject"] not in ALLOWED_SUBJECTS:
        raise ValueError("Invalid subject returned by classifier")

    return result
