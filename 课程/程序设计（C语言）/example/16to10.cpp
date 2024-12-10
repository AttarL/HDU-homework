#include<stdio.h>//为什么不输出
#include<stdlib.h>
int main(){
    int  d1,i,y;
    char h[10],a[7]={'A','B','C','D','E','F'};
    scanf("%d",&d1);
    if(d1<10){
        printf("%d",d1);
    }
    if(10<d1<=16){
        printf("%s",a[d1-10]);
    }
    else{
        y=d1/16;
        if(y<10){
        printf("%d",d1);
    }
    if(10<y<=16){
        printf("%s",a[d1-10]);
    }   
    }
    getchar();
    getchar();
    return 0;
}

#include<stdio.h>
int main() {
    int d,q,i=1,j,temp;
    char h[50];
    scanf("%d",&d);
    q= d;
    while(q!=0) {
        temp = q % 16;
        if( temp < 10)
        {temp =temp + 48; }
        else
        temp = temp + 55;
        h[i++]= temp;
        q= q/ 16;
    }
    for (j = i -1 ;j> 0;j--)
          printf("%c",h[j]);
    return 0;
}