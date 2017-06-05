/* 05/06/2017 */
#include <stdio.h>

void printRecursion(int x){
    if(x > 1){
        printRecursion(x-1);
    }
    printf("%d\n", x);
}

int main(void){
    int x;
    printf("Numbers to print: ");
    scanf("%d", &x);
    printRecursion(x);
}