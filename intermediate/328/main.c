/* 25/08/2017 */
#include <stdio.h>
#include <stdlib.h>

#define min(a, b)   ((a) < (b) ? (a) : (b));

int main(void){
    int n;
    scanf("%d", &n);
    
    int *p = malloc(n*(n+1)/2 * sizeof(int));
    for (int i = 0; i < n*(n+1)/2; i++)
        scanf("%d", p+i);
    
    for (int i = n-2; i >= 0; i--){
        for (int j = 0; j <= i; j++){
            p[i*(i+1)/2 + j] += min(p[(i+1)*(i+2)/2 + j], p[(i+1)*(i+2)/2 + j+1]);
        }
    }
    printf("%d\n", p[0]);
    free(p);
}