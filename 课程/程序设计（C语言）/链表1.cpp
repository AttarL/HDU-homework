#include<stdio.h>
#include<stdlib.h>
int main(){
int n;
scanf("%d",&n);
struct lian{
    int num;
    char c;
};
struct lian *L;
L=(struct lian*)malloc(n);
printf(sizeof(struct lian));
getchar();
getchar();
return 0;
}