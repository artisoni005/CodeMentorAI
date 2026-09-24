from services.gemini_service import generate_response


def diagnose_bug(language, code, expected_behavior, error, analysis):

    prompt = f"""
You are the Bug Diagnosis Agent of CodeMentor AI.

Your job is to identify the root cause of the bug.

Programming Language:
{language}

User's Code:
{code}

Expected Behavior:
{expected_behavior}

Error or Failing Behavior:
{error}

Code Analyzer's Analysis:
{analysis}

Based on all the information above:

1. Identify the exact bug.
2. Identify the root cause.
3. Explain why the bug occurs.
4. Explain what part of the code is responsible.
5. Explain the issue in beginner-friendly language.

Do NOT provide corrected code yet.

Focus only on diagnosis.
"""

    return generate_response(prompt)