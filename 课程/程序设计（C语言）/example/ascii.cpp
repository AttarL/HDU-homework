#include<stdio.h>
int main()
{
    int digit=0, blank=0, other=0, i=0;
    char x;
    while(i<11){
        scanf("%c", &x);
        
    if(x==' ')
            blank+=1;
    else if(x>=48&&x<=57)
        digit+=1;
    else other+=1;
        i++;
    }

    printf("digit=%d,blank=%d,other=%d", digit, blank, other-1);
    return 0;
}