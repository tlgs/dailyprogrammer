/* 21/01/2017 */
#include <stdio.h>
#include <stdlib.h>

float * step_count(float a, float b, int steps){
    float add = (b-a)/(steps-1);
    float * out = malloc(sizeof(float) * steps);
    for(int i=0; i < steps; i++)
        out[i] = a+add*i;
    return out;
}

int main(int argc, char *argv[]){
    float *myArr = step_count(strtof(argv[1], NULL), strtof(argv[2], NULL), strtol(argv[3], NULL, 10));
    for(int i=0; i < strtol(argv[3], NULL, 10); i++)
        printf("%0.3f ", myArr[i]);
}
