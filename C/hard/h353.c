/* 09/03/2018 */
// helpful: https://homes.cs.washington.edu/~armin/ACM_TECS_2013.pdf
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <time.h>

typedef int8_t stream;
#define N_BITS (sizeof(stream)*8)
#define N_RUNS 10e3

stream add(stream a, stream b, stream s){
    return (a & s) | (~s & b);
}

stream multiply(stream a, stream b){
    return (a & b);
}

stream SNG(int x){
    stream n = 0;
    for (int i = 0; i < N_BITS; i++)
        n |= ((rand()%N_BITS < x) << i);
    return n;
}

float BNG(stream x){
    int n = 0;
    for (int i = 0; i < N_BITS; i++)
        n += (x >> i) & 1;
    return (float) n/N_BITS;
}

void printStream(stream x){
    for (int i = N_BITS - 1; i >= 0; i--){
        putchar('0' + ((x >> i) & 1));
        if (i%8 == 0)  putchar(' ');
    }
}

int main(void){
    srand(time(0));

    int a, b;
    while (scanf("%d %d", &a, &b) == 2){
        float results[2] = {0};
        for (int i = 0; i < N_RUNS; i++){
            results[0] += BNG(multiply(SNG(a), SNG(b)));
            results[1] += BNG(add(SNG(a), SNG(b), SNG(N_BITS/2)))*2;
        }
        printf("%.3f * %.3f = %.3f\n", (float) a/N_BITS, (float) b/N_BITS, results[0]/N_RUNS);
        printf("%.3f + %.3f = %.3f\n", (float) a/N_BITS, (float) b/N_BITS, results[1]/N_RUNS);
    }
}