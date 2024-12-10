 #include <stdio.h>
 #include <stdlib.h>  
int su(int x){
    int i,su=3,n,flag;
for (n=1;n<x;){
    for(i=2;i<su;i++,flag=0){
        if (su%i==0) break;    //死循环了 捏吗
        else flag=1;
    }
if (flag==1){
    n++;
} 
else su=su+2;}
    return su;
}
int main(){
    int a=su(5);
    printf("1\n");
    printf("%d",a);
    printf("\n2");
    getchar();
    getchar();
    return 0;
}