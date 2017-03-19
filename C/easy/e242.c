/* 18/03/2017 */
#include <stdlib.h>
#include <stdio.h>

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
