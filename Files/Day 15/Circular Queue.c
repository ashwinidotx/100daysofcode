#include <stdio.h>
#include <stdbool.h>
#define size 5

int Qu[size];
int front=-1;
int rear=-1;

bool IsEmpty()
{
	return (front == -1 && rear == -1);
}

bool IsFull()
{
	return (rear+1)%size == front ? true : false;
}

void Enqueue(int x)
{
	printf("\nInserting %d \n", x);
	if(IsFull())
	{
		printf("Queue is Full. \n");
		return;
	}
	if(IsEmpty())
		front=rear=0;
	else
		rear=(rear+1)%size;
	Qu[rear]=x;
}

void Dequeue()
{
	printf("\nDeleting \n");
	if(IsEmpty())
	{
		printf("Queue is Empty.\n");
		return;
	}
	if(front==rear)
		rear=front=-1;
	else
		front=(front+1)%size;
}

int Front()
{
	if (front==-1)
	{
		printf("Error: Cannot return, empty Queue.\n");
		return -1;
	}
	return Qu[front];
}


void Print()
{	int index,i;
	int count = (rear+size-front)%size+1;
	printf("\nQueue: ");
	for (i = 0; i < count; i++)
	{
		index = (front+i) % size;
		printf("%d ",Qu[index]);
	}
}


int main()
{ 
   Enqueue(2);  Print();  
   Enqueue(4);  Print();  
   Enqueue(6);  Print();
   Dequeue();	Print();
   Enqueue(8);  Print();
return 0;
}