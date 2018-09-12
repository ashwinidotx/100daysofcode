#include<stdio.h>

void reverse(int *array,int size)
{
	int i,start=0,temp;
	for(i=0;i<size/2;i++)
	{
		temp=array[i];
		array[i]=array[size-i-1];
		array[size-i-1]=temp;
	}
}

int main()
{
	int array[]={11,22,33,44,55,66},end,i;
	int size=sizeof(array)/sizeof(array[0]);
	
	printf("Array: \n");
	for(i=0;i<size;i++)
		printf("%d ",array[i]);

	printf("\nCalling reverse: \n");
	reverse(array,size);
	for(i=0;i<size;i++)
		printf("%d ",array[i]);

	printf("\nCalling group reverse:\n");
	printf("enter range: ");
	scanf("%d",&end);
	reverse(array,end);
	for(i=0;i<size;i++)
		printf("%d ",array[i]);
	return 0;
}