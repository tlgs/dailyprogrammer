/* 14/05/2017 */
// Only handles values in [0, 65535]
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char * argv[]){
    unsigned short n = strtol(argv[1], NULL, 10);

    for (char i = sizeof(unsigned short)*8-1; i >= 0; i--){
        putchar('0' + ((n >> i) & 1));
        if (i%8 == 0)  putchar(' ');
    }
}
