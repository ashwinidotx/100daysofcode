/*
Problem Statement:
Given an input amount of change x,
write a function to determine the minimum number of coins
required to make that amount of change.
coinset= {100,50,20,10,5,2,1}
eg:
253= 
100*2 + 50*1 + 2*1 + 1*1 
no oc change: 5
*/

#include<stdio.h>

int main()
{
    int coin[]={100,50,20,10,5,2,1},amt,count=0,i=0,temp;
    printf("Enter amount: ");
    scanf("%d",&amt);
    temp=amt;
    //count=amt/coin[1]; amt=amt-count*coin[i];
    for (i = 0; i < 7; i++)
    {
        if (amt > 0)
        {   count+=amt/coin[i];
            amt = amt - ( coin[i] * (amt/coin[i]) );
        }
    }

    printf("\nChange: %d\n",count);
    
    return 0;
}
