/* 19/01/2017 */
#include <stdio.h>
#include <stdlib.h>

void oddSort(int *arr, int size){
    int even = size - 1,
        odd = 0;
    while(odd < even){
        while(arr[even] % 2 && even > odd)
            even--;
        while(!(arr[odd] % 2) && odd < even)
            odd++;
        int temp = arr[even];
        arr[even] = arr[odd];
        arr[odd] = temp;
    }
}

int main(int argc, char* argv[]){
    int *a = (int*) malloc((argc-1) * sizeof(int));
    for(int i = 1; i < argc; i++)
        a[i-1] = (int) strtol(argv[i], NULL, 10);
    oddSort(a, argc-1);
    for(int i = 0; i < argc-1; i++)
        printf("%d ", a[i]);
}
