/* 03/07/2017 */
#include <stdio.h>
#include <float.h>

unsigned char solveUllmans(float arr[], int size, int k, float t){
    float sum = 0;
    for(int count = 0; count < k; count++){
        float min = FLT_MAX;
        int min_index = 0;
        for(int i = 0; i < size; i++){
            if(arr[i] < min){
                min = arr[i];
                min_index = i;
            }
        }
        arr[min_index] = FLT_MAX;
        sum += min;
    }
    return sum < t;
}

int main(void){
    int n, k;
    float t;
    printf("Welcome to Ullman's puzzle.\nn: ");
    scanf("%d", &n);
    float arr[n];
    for(int i = 0; i < n; i++){
        scanf("%f", &arr[i]);
    }
    printf("t: ");
    scanf("%f", &t);
    printf("k: ");
    scanf("%d", &k);
    puts(solveUllmans(arr, n, k, t) ? "TRUE" : "FALSE");
}