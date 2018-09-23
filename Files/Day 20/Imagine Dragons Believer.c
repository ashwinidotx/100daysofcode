#include <stdio.h>

int main()
{
    char str[] = "Imagine Dragons Believer";
    for (int i = 0; i < (sizeof(str) / sizeof(str[0])); i++)
    {
        for (int j = 0; j < i; j++)
        {
            printf("%c", str[j]);
        }
        printf("\n");
    }
    for (int i = (sizeof(str) / sizeof(str[0])) - 2; i > 0; i--)
    {
        for (int j = 0; j < i; j++)
        {
            printf("%c", str[j]);
        }
        printf("\n");
    }
    return 0;
}