#include <stdio.h>
#define size 5

int queue[size], front = -1, back = -1;

void enqueue(int data)
{
    if (front == -1 && back == -1)
    {
        front++;
        back++;
        queue[back] = data;
        return;
    }
    if (back == size)
    {
        printf("Full\n");
        return;
    }
    if (back <= size)
    {
        back++;
        queue[back] = data;
    }
}
void dequeue()
{
    if (front == back)
    {
        printf("Empty.\n");
        return;
    }
    queue[front] = 0;
    front++;
}
void print()
{
    for (int i = front; i < back; i++)
        printf("%d ", queue[i]);
    printf("\n");
}

int main()
{

    printf("Enqueue x 4 and Dequeue x5.!\n");
    printf("!EN!");
    enqueue(5);
    print();
    printf("!EN!");
    enqueue(6);
    print();
    printf("!EN!");
    enqueue(7);
    print();
    printf("!EN!");
    enqueue(8);
    print();
    printf("!EN!");
    enqueue(9);
    print();

    printf("!DE!");
    dequeue();
    print();
    printf("!DE!");
    dequeue();
    print();
    printf("!DE!");
    dequeue();
    print();
    printf("!DE!");
    dequeue();
    print();
    printf("!DE!");
    dequeue();
    print();

    return 0;
}