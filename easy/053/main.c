/* 01/01/2017 */
#include <stdio.h>
#include <stdlib.h>

int * mergeAndSort(int sizeA, int a[], int sizeB, int b[]){
    int *output = (int*) malloc((sizeA + sizeB) * sizeof(int));
    int indA = 0, indB = 0;

    for(int i = 0; i < sizeA + sizeB; i++){
        if((a[indA] <= b[indB] && indA < sizeA) || indB == sizeB){
            output[i] = a[indA++];
        } else{
            output[i] = b[indB++];
        }
    }

    return output;
}

int main(){
    const char *ord[] = {"first", "second"};
    int num[2];
    int *arr[2];
    for(int i = 0; i < 2; i++){
        printf("Number of elements of %s array:", ord[i]);
        scanf("%d", &num[i]);
        printf("Insert %s array:", ord[i]);
        arr[i] = (int*) malloc(num[i] * sizeof(int));
        for(int j = 0; j < num[i]; j++){
            scanf("%d", &arr[i][j]);
        }
    }

    int *out = mergeAndSort(num[0], arr[0], num[1], arr[1]);

    for(int i = 0; i < num[0] + num[1]; i++){
        printf("%d ", out[i]);
    }
}
