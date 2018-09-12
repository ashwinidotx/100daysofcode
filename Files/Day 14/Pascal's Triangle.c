#include <stdio.h>
int main()
{
	int i,j,n,k;
	printf("Enter Num");
	scanf("%d",&n);
	for(i=1;i<=n;i++)
	{
		for(j=1;j<=i;j++)
			printf("* ");
		printf("\n");
	}

	printf("\nAnother\n");

	for(i=1;i<=n;i++,k=0)
	{
		for(j=1;j<=n-i;j++)
		{
			printf("  ");
		}
		while(k!= (2*i -1))
		{
			printf("* ");
			k++;
		}
		printf("\n");
	}
	return 0;
}

/*
for(i=1; i<=rows; ++i, k=0)
    {
        for(space=1; space<=rows-i; ++space)
        {
            printf("  ");
        }

        while(k != 2*i-1)
        {
            printf("* ");
            ++k;
        }

        printf("\n");
    }
*/