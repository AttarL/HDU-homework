#include<stdio.h>
#include<stdlib.h>
int main(){
    int n,x1,x2,y1,y2,flag=0,i=0,j=0,m,k=0,t=0;
    scanf("%d",&n);
   getchar();
    char pan[20][20],ch;
while (i<2*n){
    while (j<2*n){
    scanf("%c",&ch);
        getchar();
        pan[i][j]=ch;
    j++;}
    i++;
}
scanf("%d",&m);
while(k<m){
    scanf("%d %d %d %d",&x1,&y1,&x2,&y2);
    if((pan[x1-1][y1-1]==pan[x2-1][y2-1])&&(pan[x1-1][y1-1]!='*')){
        pan[x1-1][y1-1]=pan[x2-1][y2-1]='*';t++;
   if (t==2*n*n){printf("Congratulations!\n");break;}  
   if(t<2*n*n){
       for(i=0;i<2*n;i++){printf("%c",pan[i][0]);
    for(j=0;j<2*n;j++){
        printf(" %c",pan[i][j]);
    }printf("\n");}}}
    else {flag++;printf("Uh-oh\n");}
    if(flag==3){
        printf("Game Over\n");
      break;
    }
k++;}

return 0;}