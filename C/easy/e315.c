/* 23/05/2017 */
#include <stdio.h>
#include <stdlib.h>

unsigned int XORMult(unsigned int x, unsigned int y){
    unsigned int result = 0;
    for(int shift = 0; (y >> shift) > 0; shift++){
        if((y >> shift) & 1){
            result ^= (x << shift);
        }
    }
    return result;
}

int main(int argc, char* argv[]){
    unsigned int x = strtol(argv[1], NULL, 10);
    unsigned int y = strtol(argv[2], NULL, 10);

    printf("%u@%u=%u", x, y, XORMult(x,y));
}