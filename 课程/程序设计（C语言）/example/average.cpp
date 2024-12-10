#include <stdio.h>

double a,i,num,sum; //定义
int main() {
    num=0;
    i=0;
    sum=0; //归零
   
    while (i<10){
        scanf("%lf",&a);
        a>0?sum=sum+a:sum=sum;
        a>0?num=num+1:num=num;
        i++;
    }
    printf("%.2f", sum/num);
    return 0;
}