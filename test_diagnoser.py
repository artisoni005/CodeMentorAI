from agents.diagnoser import diagnose_bug


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

analysis = """
The program stores five integers in an array and uses a for loop
to print them. The array contains five elements with indexes 0 to 4.
The loop appears to continue until i becomes 5.
"""

result = diagnose_bug(
    "C",
    code,
    "The program should print all 5 numbers.",
    "The program accesses memory outside the array.",
    analysis
)

print(result)