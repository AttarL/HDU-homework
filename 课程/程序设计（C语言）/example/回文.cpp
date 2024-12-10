#include<stdio.h>
#include<string.h>
int main()
{
    int i;
    char str[81];
    scanf("%s",str);
    int len=strlen(str)-1;
    for(i=0;i<=len/2;i++)
    {
        if(str[i]!=str[len-i])
            break;
    }
    if(i>len/2)
        printf("yes\n");
    else
        printf("no\n");
    return 0;
}
 