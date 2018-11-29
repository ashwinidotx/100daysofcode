#include <stdio.h>
#define size 100

struct stack
{
    int stk[size];
    int top;
};
struct stack s;

void push()
{
    int num;
    if (s.top == (size - 1))
    {
        printf("Full");
        return;
    }
    scanf("%d", &num);
    s.stk[++s.top] = num;
}
int pop()
{
    if (s.top == -1)
    {
        printf("Empty");
        return (s.top);
    }
    int num = s.stk[s.top];
    printf("Popped %d .\n", num);
    s.top--;
    return num;
}
void print()
{
    int i;
    if (s.top == -1)
    {
        printf("Stack empty");
        return;
    }
    for (int i = s.top; i >= 0; i--)
    {
        printf("%d ", s.stk[i]);
    }
    printf("\n");
}
int main()
{
    s.top = -1;
    push();
    push();
    push();
    print();
    pop();
    print();
    return 0;
}