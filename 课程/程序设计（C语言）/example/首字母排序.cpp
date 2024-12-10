#include<stdio.h>
#include<string.h>
#include<stdlib.h>
int main(){
    int ret,i;
    char s1[10],s2[10],s3[10],s4[10];
      scanf("%s\n%s\n%s",&s1,&s2,&s3);
    ret=strcmp(s1,s2);
    strcpy(s4,s1);
    if (ret<0){          
        strcpy(s1,s2);
        strcpy(s2,s4); //s1>s2
    }
     
    ret=strcmp(s2,s3);
    if(ret<0){  
        strcpy(s4,s2);        
        strcpy(s2,s3); 
        strcpy(s3,s4);
    }

    ret=strcmp(s1,s2);
if (ret<0){              
        strcpy(s1,s4);
        strcpy(s2,s4);
    }
    printf("%s\n%s\n%s\n",s3,s2,s1);
    getchar();
    getchar();
    return 0;
}