#include <stdio.h>
#include <math.h>
#include <string.h>

float shannon(char* str){
    float count[128] = {0};
    float sum = 0;
    for(int i=0; i < strlen(str); i++)
        count[str[i]]++;

    for(int i=0; i < 128; i++)
        sum += count[i] ? (count[i] / strlen(str)) * log2f(count[i] / strlen(str)) : 0;

    return -1 * sum;
}

int main(int argc, char* argv[]){
    printf("%f", shannon(argv[1]));
}
