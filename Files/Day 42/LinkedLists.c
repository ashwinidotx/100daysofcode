#include <stdio.h>
#include <stdlib.h>

struct node
{
    int data;
    struct node *next;
};
struct node *head;

void insert(int value)
{
    struct node *temp = (struct node *)malloc(sizeof(struct node));
    temp->data = value;
    temp->next = head;
    head = temp;
}

void insertAtPos(int value, int pos)
{
    struct node *temp = (struct node *)malloc(sizeof(struct node));
    temp->data = value;
    if (pos == 1) // head
    {
        temp->next = head;
        head = temp;
        return;
    }
    struct node *iter = head;
    for (int i = 0; i < pos - 2; i++)
        iter = iter->next;

    temp->next = iter->next;
    iter->next = temp;
}

void print(struct node *temp)
{
    temp = head;
    while (temp != NULL)
    {
        printf("%d", temp->data);
        temp = temp->next;
        if (temp != NULL)
            printf(" -> ");
    }
    printf("\n");
}

void delete (int pos)
{
    struct node *temp = head;
    if (pos == 1) // head
    {
        head = temp->next;
        free(temp);
        return;
    }
    for (int i = 0; i < pos - 2; i++)
        temp = temp->next;
    temp->next = (temp->next)->next; // not freeing the deleted element.
}

void reverse(struct node *temp) // print in reverse.
{
    if (temp == NULL)
        return;
    reverse(temp->next);
    printf("%d ", temp->data);
}

int main()
{
    head = NULL;
    insert(66);
    insert(77);
    insert(88);
    print(head);
    insertAtPos(11, 2);
    insertAtPos(22, 1);
    insertAtPos(256, 6);
    print(head);
    delete (4);
    print(head);
    printf("\nReversed.\n");
    reverse(head);
    print(head);
    return 0;
}