#include <stdio.h>

#define min(a, b) ((a) < (b) ? (a) : (b))

int main() 
{
    int n;
    scanf("%d", &n);
    int len = n * 2 - 1;
    for(int row = 0; row < len; row++)
    {
        for(int col = 0; col < len; col++)
        {
            int m = min(row, col);
            m = min(m, len - row - 1);
            m = min(m, len - col - 1);
            printf("%d ", n - m);
        }
        printf("\n");
    }
    return 0;
}
/*
Output:
size: 5

5 5 5 5 5 5 5 5 5 
5 4 4 4 4 4 4 4 5 
5 4 3 3 3 3 3 4 5 
5 4 3 2 2 2 3 4 5 
5 4 3 2 1 2 3 4 5 
5 4 3 2 2 2 3 4 5 
5 4 3 3 3 3 3 4 5 
5 4 4 4 4 4 4 4 5 
5 5 5 5 5 5 5 5 5


*/
