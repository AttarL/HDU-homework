#include<stdio.h>
#include<string.h>
 
void  Bignum_add(char * s1,char * s2,char *s)
{    int i,j,a,l1,l2,L,t;
     
    l1=strlen(s1);
    l2=strlen(s2);
    s[0]='0';
    a=0;
    if(l1>l2) L=l1; 
    else L=l2;
    s[L+1]='\0';    
    for(i=L;l1>0&&l2>0;i--)
    {
        a=(s1[--l1]-'0')+(s2[--l2]-'0')+a/10;
        s[i]=a%10+'0';
    }
    while(l1){
        a=(s1[--l1]-'0')+a/10;
        s[i--]=a%10+'0';
            }
    while(l2){
        a=(s2[--l2]-'0')+a/10;
        s[i--]=a%10+'0';
            }
    s[i]=a/10+'0';
     
    t=0;
    while(s[t]=='0'&&t<L) t++; 
     
    strcpy(s,s+t);}
int main()
{
  int T,d=1;
  scanf("%d",&T);
 char s[1000],s1[1000],s2[1000];
  while (T--){
	scanf("%s %s",&s1,&s2);
	Bignum_add(s1,s2,s);
	printf("Case %d:\n",d++);
	printf("%s + %s = %s\n",s1,s2,s);
	if (T!=0){ printf("\n");}
  }
	return 0;
}