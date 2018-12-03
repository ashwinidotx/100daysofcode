#include <stdio.h>
#define size 5

int Queue[size], front = -1, rear = -1;

int IsFull()
{
    if ((rear + 1) % size == front)
        return 0;
    return -1;
}

int isEmpty()
{
    if (front == -1 || rear == -1)
        return 0;
    return -1;
}

void Enqueue(int data)
{
    if (IsFull() == 0)
        return;
    else if (isEmpty() == 0)
    {
        front = 0;
        rear = 0;
    }
    else
    {
        rear = (rear + 1) % size;
    }
    Queue[rear] = data;
}

void Dequeue()
{
    if (isEmpty() == 0)
        return;
    else if (front == rear)
    {
        front = 1;
        rear = 1;
    }
    else
        front = (front + 1) % size;
}

void print()
{
    for (int i = front; i <= rear; i++)
        printf("%d  ", Queue[i]);
    printf("\n");
}

int main()
{ /*
	Enqueue(55); print();
	Enqueue(66); print();
	Enqueue(77); print();
	Enqueue(88); print();
	Enqueue(99); print();
	Enqueue(100);print();
	//Dequeue(); 	 print();
	Enqueue(11); print();
	//Dequeue(); 	 print();
	Enqueue(69); print();
	//Dequeue(); 	 print();
	Dequeue(); 	 print();
	Enqueue(69); print();
*/
    Enqueue(2);
    print();
    Enqueue(4);
    print();
    Enqueue(6);
    print();
    Dequeue();
    print();
    Enqueue(8);
    print();
    Enqueue(69);
    print();
    Enqueue(70);
    print();
    Dequeue();
    print();
    Enqueue(70);
    print();
    return 0;
}