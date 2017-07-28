/* 28/07/2017 */
#include <stdio.h>
#include <stdlib.h>

int factor_sum(int x){
    int sum = 0;
    for(int i = 2; i <= x; i++){
        if(x % i == 0){
            sum += i;
            do
                x /= i;
            while(x % i == 0);
        }
    }
    return sum;
}

int main(void){
    int c;
    scanf("%d", &c);
    for(int i = 0; i < c; i++){
        int x, y;
        scanf(" (%d, %d)", &x, &y);
        printf("%s\n", factor_sum(x) == factor_sum(y) ? "VALID" : "NOT VALID");
    }
}
