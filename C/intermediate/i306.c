/* 04/05/2017 */
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char * argv[]){
    int bits = strtol(argv[1], NULL, 10);

    for(unsigned long i = 0; i < (1UL << bits); i++){
        unsigned long g = i ^ (i >> 1);
        for (int b = bits - 1; b >= 0; b--)
            putchar('0' + ((g >> b) & 1));
        putchar('\n');
    }
}
