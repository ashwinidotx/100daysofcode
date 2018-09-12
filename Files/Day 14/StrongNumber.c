#include<stdio.h>

int main()
{
	int number,i,sum=0,fact,r,temp;
	printf("Enter Number: ");
	scanf("%d",&number);
	temp=number;
	while(number)
	{
		i=1, fact=1;
		r=number%10;
		while(i<=r)
		{
			fact=fact*i;
			i++;
		}
		sum=sum+fact;
		number=number/10;
	}

	if(sum==temp)
		printf("Yes\n");
	else
		printf("No\n");
	return 0;
}
