import json
import os

from google import genai


client = genai.Client(
    api_key=os.environ["GEMINI_API_KEY"]
)

MODEL = "gemini-flash-lite-latest"


def verify_solution(question, solution, metadata):

    prompt = f"""
You are an independent STEM answer verifier.

You did NOT write the solution.

Evaluate whether the solution is correct.

QUESTION:
{question["title"]}

QUESTION BODY:
{question["body"][:6000]}

SOLUTION:
{solution[:12000]}

SUBJECT:
{metadata["subject"]}

TOPIC:
{metadata["topic"]}

Check:

1. Mathematical correctness.
2. Scientific correctness.
3. Logical reasoning.
4. Arithmetic.
5. Units where applicable.
6. Assumptions.
7. Whether the final answer follows from the work.
8. Whether important steps are missing.
9. Whether the question itself is underspecified.

Return JSON only:

{{
  "passed": true,
  "score": 0,
  "critical_error": false,
  "errors": [],
  "warnings": [],
  "required_repairs": []
}}

Scoring:

90-100 = excellent
80-89 = acceptable
70-79 = repair required
below 70 = reject

A critical mathematical or scientific error means:

"critical_error": true

Do not be generous.
Do not approve an answer merely because it sounds plausible.
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

    return json.loads(text)
