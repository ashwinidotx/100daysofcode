#include<stdio.h>
#include<stdbool.h>
#include<stdlib.h>

struct BstNode{
    int data;
    struct BstNode *left;
    struct BstNode *right;
};
struct BstNode* GetNewNode(int data)
{
    // Create new Node, Insert value, Adjust left and right links.
    struct BstNode* newNode=(struct BstNode*)malloc(sizeof(struct BstNode));
    newNode->data=data;
    newNode->left=NULL;
    newNode->right=NULL;
    return newNode;
}
struct BstNode* Insert(struct BstNode *root,int data)
{
    //3 conditions.
    //If empty, create, else data>root,data<root
    if(root==NULL)
        root=GetNewNode(data);
    else if(data<=root->data)
        root->left=Insert(root->left,data);
    else
        root->right=Insert(root->right,data);
    return root;
}

bool Search(struct BstNode *root,int data)
{
    if(root == NULL)
        return false;
    else if(root->data==data)
        return true;
    else if(root->data>data)
        return Search(root->left,data);
    else 
        return Search(root->right,data);
}
int main()
{
    printf("Binary Search Tree Implementation.");
    
    // Create Root pointer.
    struct BstNode *root=NULL;
    root = Insert(root, 15);
    root = Insert(root, 10);
    root = Insert(root, 20);
    root = Insert(root, 25);
    root = Insert(root, 8);
    root = Insert(root, 12);
    int value;
    printf("\nEnter a Value: ");
    scanf("%d",&value);

    if(Search(root,value) == true)
        printf("\nFound!");
    else
        printf("\nNot Found!");
    
    printf("\nEnd.\n");

    return 0;
}