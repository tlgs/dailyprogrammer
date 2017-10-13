/* 12/10/2017 */
#include <stdio.h>
#include <stdlib.h>

int main(void){
    int a, b;
    scanf("%d %d", &a, &b);

    for (int i=0; i < a; i++){
        unsigned char exists[100] = {0};
        unsigned char index[100];
        int sum = 0;

        for (int j=0, n; j < b; j++){
            scanf("%d", &n);
            exists[n-1] = 1;
            index[n-1] = j;

            if (n < 100 && exists[n])
                sum += abs(index[n] - index[n-1]);
            if (n > 1 && exists[n-2])
                sum += abs(index[n-2] - index[n-1]);  
        }

        printf("%d\n", sum);
    }
}