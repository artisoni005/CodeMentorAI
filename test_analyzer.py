from agents.analyzer import analyze_code


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

result = analyze_code(
    "C",
    code,
    "The program should print all 5 numbers."
)

print(result)