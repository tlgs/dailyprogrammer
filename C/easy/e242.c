/* 18/03/2017 */
#include <stdlib.h>
#include <stdio.h>

int fib(int n){
    if(n == 0 || n == 1){
        return 1;
    }
    return fib(n-1) + fib(n-2);
}

int main(int argc, char *argv[]){
    int x = strtol(argv[1], NULL, 10);
    int y = strtol(argv[2], NULL, 10);
    int weeks = 1, fruits = 0, plants = y;

    do{
        weeks ++;
        fruits += plants;
        plants += fruits;
    }while(fruits < x);

    printf("%d", weeks);
}
