#include<stdio.h>
#include<stdlib.h>
#define id_len 18
int main(){
    int n,i,sum,j;
    scanf("%d",&n);
    int weight[17]={7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2};
    char id[19];
    char m[11]={'1','0','x','9','8','7','6','5','4','3','2'};
    int flag=1;
    for(i=0;i<n;i++){
      sum=0;
      scanf("%s",id);
      for(j=0;j<17;j++){
        sum+=(id[j]-'0')*weight[j];
      }
      sum=sum%11;
      if(m[sum]!=id[17]){
        flag=0;
        printf("%s\n",id);
      }
    }
    
    if (flag==1){
    printf("All passed");
    }
    getchar();
    getchar();
    return 0;
}