from agents.reviewer import review_fix


original_code = """
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
The loop uses i <= 5, allowing i to become 5.
This causes access to numbers[5], which is outside the array.
"""

corrected_code = """
#include <stdio.h>

int main() {

    int numbers[5] = {10, 20, 30, 40, 50};

    for(int i = 0; i < 5; i++) {
        printf("%d\\n", numbers[i]);
    }

    return 0;
}
"""

result = review_fix(
    "C",
    original_code,
    diagnosis,
    corrected_code,
    "The program should print all 5 numbers."
)

print(result)