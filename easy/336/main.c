/* 17/10/2017 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int cmp_int (const void * a, const void * b){
    return (*(int*)b - *(int*)a);
}

int main(void){
    int i, j;
    scanf("%d %d", &i, &j);
    int values[i], queries[j];
    for (int k=0; k < i; k++)
        scanf("%d", &values[k]);
    for (int k=0; k < j; k++)
        scanf("%d", &queries[k]);

    qsort(values, i, sizeof(int), cmp_int);
    for (int k=0; k < j; k++){
        int arr[i], top = 0, bottom = i, result = 0;
        memcpy(arr, values, i*sizeof(int));
        while (top < bottom){
            if (arr[top] >= queries[k]){
                result++;
                top++;
            }
            else{
                arr[top]++;
                bottom--;
            }
        }
        printf("%d ", result);
    }
}