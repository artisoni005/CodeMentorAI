import streamlit as st

from agents.analyzer import analyze_code
from agents.diagnoser import diagnose_bug
from agents.fixer import suggest_fix
from agents.reviewer import review_fix


st.set_page_config(
    page_title="CodeMentor AI",
    page_icon="💻",
    layout="wide"
)


# -----------------------------
# Page Styling
# -----------------------------

st.markdown(
    """
    <style>
    .main-title {
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 0px;
    }

    .subtitle {
        font-size: 18px;
        color: #666;
        margin-bottom: 25px;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# -----------------------------
# Header
# -----------------------------

st.markdown(
    '<div class="main-title">💻 CodeMentor AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">AI Coding Mentor & Debugging Assistant</div>',
    unsafe_allow_html=True
)

st.write(
    "Understand your bugs instead of simply receiving a replacement solution."
)


# -----------------------------
# Sidebar
# -----------------------------

with st.sidebar:

    st.header("⚙️ Debugging Settings")

    language = st.selectbox(
        "Programming Language",
        [
            "C",
            "C++",
            "Python",
            "Java",
            "JavaScript"
        ]
    )

    explanation_mode = st.selectbox(
        "Explanation Mode",
        [
            "Beginner",
            "Advanced"
        ]
    )

    debugging_mode = st.radio(
        "Execution Mode",
        [
            "Demo Mode",
            "Live AI Mode"
        ]
    )

    debugging_style = st.radio(
        "Debugging Style",
        [
            "Normal Mode",
            "Hint Mode"
        ]
    )

    st.divider()

    st.subheader("🤖 Agent Pipeline")

    st.write("1. 🔎 Code Analyzer")
    st.write("2. 🐛 Bug Diagnoser")
    st.write("3. 🔧 Fix Agent")
    st.write("4. 🧐 Reviewer")

    st.divider()

    if debugging_mode == "Demo Mode":
        st.info(
            "Demo Mode does not use the Gemini API. "
            "It is useful for demonstrating the complete workflow."
        )
    else:
        st.info(
            "Live AI Mode uses Gemini to analyze and debug your code."
        )


# -----------------------------
# User Input
# -----------------------------

st.header("📝 Submit Your Code")

code = st.text_area(
    "Paste your code",
    height=300,
    placeholder="Paste your program here..."
)

expected_behavior = st.text_area(
    "What should your program do?",
    height=120,
    placeholder="Example: The program should read 5 numbers and print their average."
)

error = st.text_area(
    "Error Message / Failing Behavior",
    height=120,
    placeholder="Paste the error message or describe what is going wrong."
)


debug_button = st.button(
    "🔍 Debug My Code",
    type="primary",
    use_container_width=True
)


# ==========================================================
# DEMO MODE
# ==========================================================

def run_demo():

    analysis = """
## What the Program Is Trying to Do

The program stores 5 numbers inside an integer array and uses a
for loop to print all the numbers.

## Important Data Structure

The program uses:

`int numbers[5]`

This array contains 5 elements.

The valid indexes are:

`0, 1, 2, 3, 4`

## Main Control Flow

The program starts from `main()`.

It creates the array and then uses a for loop to access each
element and print it.

## Potentially Problematic Section

The loop condition is:

`i <= 5`

This allows `i` to become 5.

However, index 5 does not exist in an array of size 5.
"""

    diagnosis = """
## Exact Bug

The problem is in the loop condition:

`i <= 5`

## Root Cause

The array contains 5 elements, but C array indexing starts from 0.

Therefore, the valid indexes are:

`0, 1, 2, 3, 4`

When `i` becomes 5, the program tries to access:

`numbers[5]`

This is outside the valid array range.

## Why This Happens

The loop should stop before `i` reaches 5.

The condition `i <= 5` includes 5.

The condition `i < 5` stops the loop at 4.

## Beginner Explanation

Think of an array with 5 boxes.

The boxes are numbered:

`0 → 1st box`
`1 → 2nd box`
`2 → 3rd box`
`3 → 4th box`
`4 → 5th box`

There is no box numbered 5.

Therefore, the loop must use:

`i < 5`
"""

    fix = """
## Required Change

Change:

`i <= 5`

to:

`i < 5`

## Why This Fix Works

The loop will now run for:

`i = 0`
`i = 1`
`i = 2`
`i = 3`
`i = 4`

These are exactly the five valid array indexes.

## Corrected Code

```c
#include <stdio.h>

int main() {

    int numbers[5] = {10, 20, 30, 40, 50};

    for(int i = 0; i < 5; i++) {
        printf("%d\\n", numbers[i]);
    }

    return 0;
}
````

## Explanation

The corrected loop accesses only valid elements of the array.

The program will print all five numbers without accessing memory
outside the array.
"""

    review = """


## Fix Validation

The proposed correction changes the loop condition from:

`i <= 5`

to:

`i < 5`

## Does It Solve the Bug?

Yes.

The loop now accesses only:

`numbers[0]`
`numbers[1]`
`numbers[2]`
`numbers[3]`
`numbers[4]`

These are all valid indexes.

## New Issues

No important new issue was introduced by this correction.

## Final Recommendation

The correction properly solves the array boundary problem.

The program should now print:

10
20
30
40
50
"""


    return analysis, diagnosis, fix, review

# ==========================================================

# DEBUG BUTTON

# ==========================================================

if debug_button:


    if not code.strip():

        st.warning("⚠️ Please enter your code.")

    elif not expected_behavior.strip():

        st.warning("⚠️ Please describe the expected behavior.")

    elif not error.strip():

        st.warning("⚠️ Please provide the error or failing behavior.")

    else:

        st.header("🤖 AI Debugging Process")

    # -----------------------------
    # Demo Mode
    # -----------------------------


    if debugging_mode == "Demo Mode":

        analysis, diagnosis, fix, review = run_demo()

        # -----------------------------------
        # Analyzer
        # -----------------------------------

        with st.status(
            "🔎 Code Analyzer Agent",
            expanded=True
        ):
            st.write("Analyzing program structure...")
            st.success("Code analysis completed.")

        # -----------------------------------
        # Diagnoser
        # -----------------------------------

        with st.status(
            "🐛 Bug Diagnoser Agent",
            expanded=True
        ):
            st.write("Finding the root cause...")
            st.success("Bug diagnosis completed.")

        # -----------------------------------
        # Show Analysis
        # -----------------------------------

        st.header("📊 Debugging Report")

        with st.expander(
            "🔎 1. Code Understanding & Analysis",
            expanded=True
        ):
            st.markdown(analysis)

        with st.expander(
            "🐛 2. Bug Diagnosis",
            expanded=True
        ):
            st.markdown(diagnosis)

        # -----------------------------------
        # HINT MODE
        # -----------------------------------

        if debugging_style == "Hint Mode":

            st.header("💡 Debugging Hint")

            st.info(
                """
                Think carefully about the loop condition.

                The array contains 5 elements.

                Ask yourself:

                • What is the first valid array index?
                • What is the last valid array index?
                • What happens when the loop reaches 5?
                • Should the loop use <= or < ?
                """
            )

            st.warning(
                "🔒 Hint Mode hides the corrected code. "
                "Try to fix the problem yourself."
            )

            st.success(
                "💡 Use the diagnosis above to find the solution."
            )

        # -----------------------------------
        # NORMAL MODE
        # -----------------------------------

        else:

            # -----------------------------------
            # Fix Agent
            # -----------------------------------

            with st.status(
                "🔧 Fix Agent",
                expanded=True
            ):
                st.write("Generating a correction...")
                st.success("Suggested fix generated.")

            # -----------------------------------
            # Reviewer Agent
            # -----------------------------------

            with st.status(
                "🧐 Reviewer Agent",
                expanded=True
            ):
                st.write(
                    "Checking whether the correction solves the problem..."
                )
                st.success("Fix review completed.")

            # -----------------------------------
            # Show Fix
            # -----------------------------------

            with st.expander(
                "🔧 3. Suggested Fix",
                expanded=True
            ):
                st.markdown(fix)

            # -----------------------------------
            # Show Review
            # -----------------------------------

            with st.expander(
                "🧐 4. Fix Validation & Review",
                expanded=True
            ):
                st.markdown(review)

                
            st.subheader("🧪 Test Case Generator")

            demo_test_cases = """
                ## Normal Test Cases

                **Test Case 1**
                - Input: `{10, 20, 30, 40, 50}`
                - Expected: All 5 numbers should be printed.
                - Purpose: Checks normal array traversal.

                **Test Case 2**
                - Input: `{1, 2, 3, 4, 5}`
                - Expected: All 5 numbers should be printed.
                - Purpose: Checks traversal with different values.

                ## Edge Cases

                **Test Case 3**
                - Input: Array containing negative numbers.
                - Expected: All valid elements should be printed.
                - Purpose: Checks whether the loop works with negative values.

                **Test Case 4**
                - Input: Array containing zero.
                - Expected: Zero should be printed correctly.
                - Purpose: Checks boundary values.

                ## Expected Results

                The loop should access indexes:

                `0 → 1 → 2 → 3 → 4`

                It should **not** access index `5`.

                ## What These Tests Verify

                These test cases verify that the corrected loop processes exactly the five elements of the array and does not access memory outside the array boundary.
                """

            with st.expander("View Generated Test Cases", expanded=True):
                
                st.markdown(demo_test_cases)


            st.success(
                "🎉 Complete debugging workflow demonstrated successfully!"
            )


    # -----------------------------
    # Live AI Mode
    # -----------------------------

    else:

        try:

            with st.status(
                "🔎 Code Analyzer Agent is analyzing your code...",
                expanded=True
            ):

                analysis = analyze_code(
                    language,
                    code,
                    expected_behavior
                )

                st.write("✅ Code analysis completed.")


            with st.status(
                "🐛 Bug Diagnosis Agent is identifying the root cause...",
                expanded=True
            ):

                diagnosis = diagnose_bug(
                    language,
                    code,
                    expected_behavior,
                    error,
                    analysis
                )

                st.write("✅ Bug diagnosis completed.")


            with st.status(
                "🔧 Fix Agent is generating a correction...",
                expanded=True
            ):

                fix = suggest_fix(
                    language,
                    code,
                    diagnosis
                )

                st.write("✅ Suggested fix generated.")


            with st.status(
                "🧐 Reviewer Agent is validating the fix...",
                expanded=True
            ):

                review = review_fix(
                    language,
                    code,
                    diagnosis,
                    fix,
                    expected_behavior
                )

                st.write("✅ Fix review completed.")


            st.header("📊 Debugging Report")

            with st.expander(
                "🔎 1. Code Understanding & Analysis",
                expanded=True
            ):
                st.markdown(analysis)

            with st.expander(
                "🐛 2. Bug Diagnosis",
                expanded=True
            ):
                st.markdown(diagnosis)

            with st.expander(
                "🔧 3. Suggested Fix",
                expanded=True
            ):
                st.markdown(fix)

            with st.expander(
                "🧐 4. Fix Validation & Review",
                expanded=True
            ):
                st.markdown(review)

            st.success(
                "🎉 Live AI debugging workflow completed successfully!"
            )


        except Exception as e:

            error_message = str(e)

            if (
                "429" in error_message
                or "RESOURCE_EXHAUSTED" in error_message
            ):

                st.error(
                    "⚠️ Gemini API quota has been exhausted."
                )

                st.info(
                    "Switch to Demo Mode to demonstrate the "
                    "complete debugging workflow without using "
                    "the Gemini API."
                )

            elif (
                "503" in error_message
                or "UNAVAILABLE" in error_message
            ):

                st.error(
                    "⚠️ Gemini is temporarily unavailable."
                )

                st.info(
                    "Please wait and try Live AI Mode again later."
                )

            else:

                st.error(
                    "❌ Something went wrong while debugging."
                )

                st.code(error_message)


# -----------------------------

# Footer

# -----------------------------

st.divider()

st.caption(
"CodeMentor AI | AI Coding Mentor & Debugger"
)

st.caption(
"Analyze → Diagnose → Fix → Review"
)
