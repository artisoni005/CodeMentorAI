from agents.workflow import run_debugging_workflow


code = """
#include <stdio.h>

int main() {

    int numbers[5] = {10, 20, 30, 40, 50};

    for(int i = 0; i <= 5; i++) {
        printf("%d\\n", numbers[i]);
    }

    return 0;
}
"""


result = run_debugging_workflow(
    "C",
    code,
    "The program should print all 5 numbers.",
    "The program accesses memory outside the array."
)


print("\n========== CODE ANALYSIS ==========\n")
print(result["analysis"])

print("\n========== BUG DIAGNOSIS ==========\n")
print(result["diagnosis"])

print("\n========== FIX ==========\n")
print(result["fix"])

print("\n========== REVIEW ==========\n")
print(result["review"])