from services.gemini_service import generate_response


def analyze_code(language, code, expected_behavior):

    prompt = f"""
You are the Code Analyzer Agent of CodeMentor AI.

Analyze the following program before attempting to fix it.

Programming Language:
{language}

Code:
{code}

Expected Behavior:
{expected_behavior}

Provide:

1. What the program is trying to do
2. Important variables and data structures
3. Main control flow
4. Potentially problematic sections
5. Any logical or syntax concerns

Do NOT provide corrected code yet.

Explain everything in beginner-friendly language.
"""

    return generate_response(prompt)