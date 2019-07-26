// Header file for input output functions
#include <stdio.h>
#include "utils.h"

int main(void)
{
    int a = 10, b = 20;

    // Calling above function to find max of 'a' and 'b'
    int m = max(a, b);

    printf("compared values: %d and %d", a, b);
    printf("\n");
    printf("max is %d", m);
    printf("\n");

    return 0;
}
