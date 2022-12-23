/* 05/05/2017 */
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

int main(void){
    srand(time(NULL));

    char pieces[] = "OISZLJT";
    char bag[] = "OISZLJT";

    for(int i = 0; i < 50; i++){
        char pc = i%7;
        if(!pc){
            memcpy(bag, pieces, 7);
        }

        char index = rand()%(7-pc);
        putchar(bag[index]);
        bag[index] = bag[6-pc];
    }
}
