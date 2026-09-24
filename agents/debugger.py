from services.gemini_service import generate_response
from prompts.debugging_prompts import DEBUGGING_PROMPT


def debug_code(language, code, expected_behavior, error):

    prompt = DEBUGGING_PROMPT.format(
        language=language,
        code=code,
        expected_behavior=expected_behavior,
        error=error
    )

    result = generate_response(prompt)

    return result