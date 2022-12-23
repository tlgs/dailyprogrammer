/* 04/03/2017 */
#include <stdio.h>
#include <stdlib.h>

int rot(int n){
    int x = n, c = 0;
    while(x > 1){x = x >> 1; c++;}
    return (n & 0b1) << c | (n >> 1);
}

int main(int argc, char *argv[]){
    int n = strtol(argv[1], 0, 10);
    while(n != rot(n)){
        printf("%d -> ", n);
        n = rot(n);
    } printf("%d", n);
}
