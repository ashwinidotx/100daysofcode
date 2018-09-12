#include<stdio.h>
#include<math.h>
int main()
{
    int num,temp,ans=0,rem,digit=0;
    printf("Enter a number:");
    scanf("%d",&num);

    temp=num;
    while(temp!=0)
    {
        temp=temp/10;
        digit++;
    }
    printf("\nDigit: %d\n",digit);
    // Step 2------------------------------

    temp=num;

    while(temp!=0)
    {   //printf("hi  ");
        rem=temp%10;
        ans=ans+pow(rem,digit);
        temp=temp/10;
    }
    printf("\n%d ",ans);
    if(ans==num)
        printf("\nYes");
    else
        printf("No");

    printf("\nEnd.\n");

    return 0;
}