#include <stdio.h>
int main() {
    int year;
    int month;
    int day;
    scanf("%d-%d-%d", &year, &month, &day);
    if (year==2021&&month>9||year>2021){
        if (year==2021&&month>9||year>2021){
    if (month < 1 || month>12) {
        printf("no");
    }
    else if (month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10 || month == 12) {
        if (day >= 1 && day <= 31) {
            printf("yes");
        }
        else {
            printf("no");
        }
    }
    else if (month == 4 || month == 6 || month == 9 || month == 11) {
        if (day >= 1 && day <= 30) {
            printf("yes");
        }
        else {
            printf("no");
        }
    }                   
    else if ((year % 100 != 0 && year % 4 == 0) || year % 400 == 0) {
        if (day >= 1 && day <= 29) {
            printf("yes");
        }
        else{
            printf("no");
        }
    }
    else {
        if (day >= 1 && day <= 28) {
            printf("yes");
        }
        else {
            printf("no");
        }
    }}
    else{ 
        if(day>9)printf("yes");
        else printf("no");}}
    else printf("no");
    return 0;
}
