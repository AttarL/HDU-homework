#include<stdio.h>
#include<stdlib.h>
main(){
    int a[5][5];
    int i,j;
    for(i=0;i<5;i++){
        a[i][0]=1;
        a[i][i]=1;
    }
    for(i=1;i<4;i++)
    for(j=1;j<i;j++){
        a[i][j]=a[i-1][j-1]+a[i-1][j];
    }
     for(i=0;i<5;i++){
        for(j=0;j<5;j++){
    if (j<=i){
     printf("%d ",a[i][j]);}}
        printf("\n");
    }
    getchar();
    getchar();
    return 0;}
