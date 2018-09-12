#include<stdio.h>
#include <math.h>
void prime(int num)
{
	int i,j,count,number=0;

	for(i=2; i<=num; i++)
	{	
		count=0;
		for(j=1; j<=sqrt(i); j++)
		{
			if(i%j==0)
				count++;
		}

		if(count==1)
			{
				printf("%d ",i);
				number++;
			}
	}

	printf("\nTotal numbers: %d\n",number);
}

int main()
{
	int num;
	printf("Enter Range: ");
	scanf("%d",&num);
	prime(num);
	
	return 0;
}