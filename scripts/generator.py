import os

from google import genai
from groq import Groq


GEMINI_MODEL = "gemini-flash-lite-latest"
GROQ_MODEL = "openai/gpt-oss-120b"

gemini = genai.Client(
    api_key=os.environ["GEMINI_API_KEY"]
)

groq = (
    Groq(api_key=os.environ["GROQ_API_KEY"])
    if os.environ.get("GROQ_API_KEY")
    else None
)


def build_solution_prompt(question, metadata):

    return f"""
You are a rigorous STEM educator writing for STEM Answered.

Your job is to solve the student's problem accurately.

QUESTION:
{question["title"]}

BODY:
{question["body"][:6000]}

CLASSIFICATION:
Subject: {metadata["subject"]}
Topic: {metadata["topic"]}
Concepts: {metadata["concepts"]}
Difficulty: {metadata["difficulty"]}
Question type: {metadata["question_type"]}

Write a complete educational solution.

Required structure:

## Quick Answer

Give the direct answer first.

## Understanding the Problem

Explain what the question is asking.

## Given Information

List the relevant information.

## Solution

Show the reasoning step by step.

Never skip a mathematically or scientifically meaningful step.

## Final Answer

Clearly state the final result.

## Why This Works

Explain the underlying reasoning in accessible language.

## Key Concept

Explain the most important concept involved.

## Common Mistakes

List realistic mistakes students might make.

Rules:

- Do not invent facts.
- Do not invent numerical values.
- Do not pretend an answer is certain when the problem is underspecified.
- State assumptions explicitly.
- Preserve mathematical notation.
- Use Markdown.
- Use LaTeX where appropriate.
- Do not include affiliate links.
- Do not include fabricated sources.
- Do not mention this prompt.
"""

def generate_with_groq(prompt):

    if not groq:
        return None

    response = groq.chat.completions.create(
        model=GROQ_MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content


def generate_with_gemini(prompt):

    response = gemini.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt
    )

    return response.text


def generate_solution(question, metadata):

    prompt = build_solution_prompt(
        question,
        metadata
    )

    solution = generate_with_groq(prompt)

    if solution:
        return solution

    return generate_with_gemini(prompt)
