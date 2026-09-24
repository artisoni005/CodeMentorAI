from services.gemini_service import generate_response


def review_fix(language, original_code, diagnosis, corrected_code, expected_behavior):

    prompt = f"""
You are the Reviewer Agent of CodeMentor AI.

Your job is to review a proposed code correction.

Programming Language:
{language}

Original Code:
{original_code}

Expected Behavior:
{expected_behavior}

Bug Diagnosis:
{diagnosis}

Proposed Corrected Code:
{corrected_code}

Review the proposed correction carefully.

Check:

1. Does the correction address the diagnosed bug?
2. Does the corrected code satisfy the expected behavior?
3. Did the correction introduce any new problems?
4. Is the correction logically correct?
5. Are there any additional important issues?

Return your answer using exactly these sections:

## Fix Validation

## Does It Solve the Bug?

## New Issues

## Final Recommendation

Explain everything in beginner-friendly language.
"""

    return generate_response(prompt)