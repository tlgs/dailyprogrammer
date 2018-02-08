/* 08/02/2018 */
#include <stdio.h>

int main(void){
    int n;
    scanf("%d", &n);
    int items[n], sums[n];
    for (int i=0; i < n; i++){
        scanf("%d", &items[i]);
        sums[i] = i == 0 ? 0 : sums[i-1] + items[i-1];
    }
    for (int i=0; i < n; i++){
        if (sums[i] == sums[n-1] + items[n-1] - sums[i] - items[i])
            printf("%d ", i);
    }
}