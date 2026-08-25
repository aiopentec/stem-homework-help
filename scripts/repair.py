def build_repair_prompt(
    question,
    solution,
    verification
):

    return f"""
Repair the following STEM solution.

QUESTION:
{question["title"]}

ORIGINAL SOLUTION:
{solution}

VERIFICATION REPORT:
{verification}

Fix every identified mathematical,
scientific, logical, numerical, or explanatory problem.

Do not introduce new unsupported claims.

Return the complete corrected solution.

Use this structure:

## Quick Answer

## Understanding the Problem

## Given Information

## Solution

## Final Answer

## Why This Works

## Key Concept

## Common Mistakes
"""
