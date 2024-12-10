#include<stdio.h>
int main(){
    int i,n,m,min,max;
scanf("%d",&n);
max=min=n;
    for(i=0;i<9;i++){
        scanf("%d",&m);
        m>max?max=m:max=max;
        m<min?min=m:min=min;
    }
printf("%d",max-min);
return 0;}