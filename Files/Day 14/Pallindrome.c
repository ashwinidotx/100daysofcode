#include<stdio.h>
#include<stdbool.h>
bool isPallindrome(int number)
{
    int temp = number,pallin=0;
    while (temp != 0)
    {
        pallin = pallin * 10 + temp % 10;
        temp = temp / 10;
    }
    if (pallin==number)
        return true;
    else
        return false;
    
}
int main()
{

    int number,pallin=0;
    printf("Enter a number:");
    scanf("%d",&number);
    if(isPallindrome(number)==true)
        printf("\nyes");
    else
        printf("\nno.");
    return 0;
}