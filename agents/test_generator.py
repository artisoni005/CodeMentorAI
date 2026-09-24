from services.gemini_service import generate_response


def generate_test_cases(language, code, expected_behavior, diagnosis):
    prompt = f"""
You are the Test Case Generator Agent of CodeMentor AI.

Your job is to create useful test cases for the user's program after a bug has been diagnosed.

Programming Language:
{language}

Code:
{code}

Expected Behavior:
{expected_behavior}

Bug Diagnosis:
{diagnosis}

Generate:

1. Normal test cases
2. Edge cases
3. Expected result for each test case
4. A short explanation of what each test checks

Focus on helping a beginner verify whether the bug has been fixed.

Return the answer using these sections:

## Normal Test Cases

## Edge Cases

## Expected Results

## What These Tests Verify

Keep the explanation beginner-friendly.
"""

    return generate_response(prompt)
