/* 05/03/2018 */
#include <stdio.h>
#include <stdlib.h>

void printBase62(unsigned long long n){
    const char base[] = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    if (n / 62 > 0)
        printBase62(n / 62);
    putchar(base[n % 62]);
}

int main(int argc, char* argv[]){
    unsigned long long n = strtoull(argv[1], NULL, 0);
    printBase62(n);
}