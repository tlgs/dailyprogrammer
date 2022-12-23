/* 20/06/2017 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

void getFibonacci(unsigned long long* arr, int n){
    arr[0] = 1;
    arr[1] = 1;
    for(int i = 2; i < n; i++){
        arr[i] = arr[i-1] + arr[i-2];
    }
}

void toBaseFib(char* value, char* result){
    unsigned long long n = strtoull(value, NULL, 10);
    double temp = n * sqrt(5) + 0.5;
    int size = (int) (log(temp) / log(1.61803398875));
    unsigned long long* fibonacci = malloc(sizeof(unsigned long long) * size);
    getFibonacci(fibonacci, size);

    for(int i = 0; i < size; i++){
        unsigned long long F = fibonacci[size-i-1];
        if(n >= F){
            n -= F;
            result[i] = '1';
        }
        else{
            result[i] = '0';
        }
    }
    result[size] = '\0';
}

void toBaseDec(char* value, char* result){
    int size = strlen(value);
    unsigned long long* fibonacci = malloc(sizeof(unsigned long long) * size);
    getFibonacci(fibonacci, size);

    unsigned long long sum = 0;
    for(int i=0; i < size; i++){
        if(value[i] == '1'){
            sum += fibonacci[size-i-1];
        }
    }
    sprintf(result, "%llu", sum);
}


int main(int argc, char* argv[]){
    if(argc != 3){
        printf("This program takes TWO arguments.\n");
        return EXIT_FAILURE;
    }

    char base[8], value[32];
    strcpy(base, argv[1]);
    strcpy(value, argv[2]);

    if(strcmp(base, "F") && strcmp(base, "10")){
        printf("Invalid base.\n");
        return EXIT_FAILURE;
    }

    char result[32];
    !strcmp(base, "10") ? toBaseFib(value, result) : toBaseDec(value, result);
    puts(result);
}