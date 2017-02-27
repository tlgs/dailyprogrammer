/* 27/02/2017 */

#include <stdio.h>

char checkDigits(int num){
    char digits[4] = {};
    for(int i = 0; i < 4; i++){
        digits[i] = num%10;
        for(int j = i-1; j >= 0; j--){
            if(digits[i] == digits[j])
                return 1;
        }
        num /= 10;
    }
    return 0;
}

int main(){
    for(int num = 1000; num < 10000; num++){
        if(checkDigits(num)) continue;
        int sum = num/100 + num%100;
        if(sum*sum == num)
            printf("%d\n", num);
    }
}
