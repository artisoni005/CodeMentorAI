from agents.analyzer import analyze_code
from agents.diagnoser import diagnose_bug
from agents.fixer import suggest_fix
from agents.reviewer import review_fix
from agents.test_generator import generate_test_cases

def run_debugging_workflow(
    language,
    code,
    expected_behavior,
    error
):

    analysis = analyze_code(
        language,
        code,
        expected_behavior
    )

    diagnosis = diagnose_bug(
        language,
        code,
        expected_behavior,
        error,
        analysis
    )

    fix = suggest_fix(
        language,
        code,
        diagnosis
    )

    corrected_code = fix

    review = review_fix(
        language,
        code,
        diagnosis,
        corrected_code,
        expected_behavior
    )

    return {
        "analysis": analysis,
        "diagnosis": diagnosis,
        "fix": fix,
        "review": review
    }