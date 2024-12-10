#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(){
    int i,j,num,m;
    char a[501],t; 
    scanf("%d",&m);
    while(m--){
        scanf("%s",&a);
        num=strlen(a);
        printf("%s",a);
    for(j=1;j<num;j++){
        t=a[0];
        for(i=1;i<num;i++)
        a[i-1]=a[i];
        a[num-1]=t;
        if (i!=num-1)printf(" %s",a);
        else printf("%s",a);
    }if(m-1>0){printf("\n");}
    }
    getchar();
    getchar();
    return 0;
}

