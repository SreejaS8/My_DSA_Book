#include <stdio.h>
#include <math.h>

// Helper function to check if a number is a perfect square
int is_perfect_square(int x) {
    int s = (int)sqrt(x);
    return (s * s == x);
}

// Function to check if a number is a Fibonacci number
int is_fibonacci(int n) {
    // A number is Fibonacci if and only if one of (5*n^2 + 4) or (5*n^2 - 4) is a perfect square
    return is_perfect_square(5 * n * n + 4) || is_perfect_square(5 * n * n - 4);
}

// Function to print non-Fibonacci numbers in a given range
void print_non_fibonacci(int start, int end) {
    for (int i = start; i <= end; i++) {
        if (!is_fibonacci(i)) {
            printf("%d ", i);
        }
    }
    printf("\n");
}

int main() {
    int start, end;

    // Input the range from the user
    printf("Enter the start of the range: ");
    scanf("%d", &start);
    printf("Enter the end of the range: ");
    scanf("%d", &end);

    // Print non-Fibonacci numbers in the range
    print_non_fibonacci(start, end);

    return 0;
}
