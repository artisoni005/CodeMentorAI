from agents.fixer import suggest_fix


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

diagnosis = """
The array contains 5 elements, so valid indexes are 0 to 4.
The for loop uses i <= 5, which allows i to become 5.
This causes the program to access numbers[5], which is outside
the valid array range.
"""

result = suggest_fix(
    "C",
    code,
    diagnosis
)

print(result)