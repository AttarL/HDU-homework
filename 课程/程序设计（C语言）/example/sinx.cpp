#include<stdio.h>
#include<math.h>
int jie(int n){
    int i,sum=1;
    for(i=1;i<=n;i++){
sum=i*sum;
    }
    return sum;
}
double cheng(int n,double x){
    int i;
    double sum=1;
    for(i=1;i<=n;i++){
        sum=sum*x;
    }
    return sum;
}

int main(){
    double x;
    scanf("%lf",&x);
    double i,sum=0,y;
    int n,m;
    for(n=1;n>0;n++){
    m=jie(2*n-1);
    y=cheng(2*n-1,x);
i=pow(-1,n+1)*y/m;
sum=sum+i;
if (i<0.00001){
    printf("%.4lf",sum);
    break;
}
    }
    return 0;
}