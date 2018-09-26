#include<stdio.h>
#include<string.h>
int main()
{
int i,n;
char output[100]=" ";
printf("Enter Range: ");
scanf("%d",&n);
for(i=1;i<=n;i++)
{
    char s[] = {'0' + i, '\0'};
    if(i%3==0)
        strcat(output,"Fizz ");
    else if(i%5==0)
        strcat(output,"Buzz ");
    else
        strcat(strcat(output,s)," ");
}
puts(output);
return 0;
}