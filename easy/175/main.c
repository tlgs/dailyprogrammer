/* 10/01/2017 */

#include <stdio.h>
#include <time.h>
#include <string.h>
#include <stdlib.h>

void shuffle(char arr[], int size){
    char *fixed = malloc(size * sizeof(char));
    memcpy(fixed, arr, size * sizeof(char));
    for(int i = size; i > 0; i--){
        int index = rand()%i;
        arr[size - i] = fixed[index];
        fixed[index] = fixed[i - 1];
    }
}

int bogoSort(char arr[], char sorted[], int size){
    int count = 0;
    while(!(strcmp(arr, sorted) == 0)){
        shuffle(arr, size-1);
        count++;
    }
    return count;
}

int main(void){
    srand(time(NULL));
    char a[] = "lolhe", b[] = "hello";
    int num = bogoSort(a, b, sizeof(a)/sizeof(a[0]));
    printf("Number of iterations: %d\n%s", num, a);
}
