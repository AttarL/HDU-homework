#include <stdio.h>
#include <string.h>
#include <windows.h>
#include <stdlib.h> //for getchar
#include <iostream>
using namespace std;

int main()
{   
    string s;  
    getline(cin,s);
    printf("Hello,%s",s.c_str());
    return 0;
}