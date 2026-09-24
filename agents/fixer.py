from services.gemini_service import generate_response


def suggest_fix(language, code, diagnosis):

    prompt = f"""
You are the Fix Agent of CodeMentor AI.

Your job is to suggest a correction for the diagnosed bug.

Programming Language:
{language}

Original Code:
{code}

Bug Diagnosis:
{diagnosis}

Follow these steps:

1. Explain exactly what needs to be changed.
2. Explain why the change fixes the problem.
3. Provide the corrected code.
4. Keep the explanation beginner-friendly.
5. Do not introduce unnecessary changes to the original program.

Return your answer using these sections:

## Required Change

## Why This Fix Works

## Corrected Code

## Explanation
"""

    return generate_response(prompt)