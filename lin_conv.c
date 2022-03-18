#include <stdio.h>
void main()
{
    float y[12];
    int m = 6, n = 6, i, j;
    float x[11] = {1, 2, 3, 4, 5, 6, 0, 0, 0, 0, 0};
    float h[11] = {1, 2, 3, 4, 5, 6, 0, 0, 0, 0, 0};

    for (i = 0; i < m + n - 1; i++)
        for (j = 0; j <= i; j++)
            y[i] = y[i] + x[j] * h[i - j];

    for (i = 0; i < m + n - 1; i++)
        printf("%f \n", y[i]);
}
