#include <stdio.h>
#include <string.h>
#define MAX 100

int main() {
    char str[MAX];
    char stack[MAX];
    int top = -1;
    int countA = 0, countB = 0;

    printf("Enter a String: ");
    scanf("%s", str);

    for (int i = 0; str[i]; i++) {
        stack[++top] = str[i];
    }

    while (top >= 0) {
        char c = stack[top--];
        if (c == 'a') countA++;
        else if (c == 'b') countB++;
    }

    printf("'a's: %d, 'b's: %d - They are %sequal\n", countA, countB, (countA == countB) ? "" : "not ");
    return 0;
}
