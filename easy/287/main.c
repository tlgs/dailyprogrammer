/* 29/01/2017 */
#include <stdio.h>
#include <stdlib.h>

#define KAPREKAR_CONST 6174

int _pow(int base, int exp){
    return exp == 0 ? 1 : base * _pow(base, exp - 1);
}

char largest_digit(short num, char *index){
    char max = 0;
    for(char i = 0; i < 4; i++){
        if(num%10 > max){
            max = num%10;
            if(index) *index = i;
        }
        num /= 10;
    }
    return max;
}

short desc_digits(short num){
    int out[4];
    for(char i = 0, p; i < 4; i++){
        out[i] = largest_digit(num, &p);
        num -= (out[i]) * _pow(10, p);
    }
    return out[0]*1000 + out[1]*100 + out[2]*10 + out[3];
}

short asc_digits(short num){
    short out[4];
    for(char i = 3, p; i >= 0; i--){
        out[i] = largest_digit(num, &p);
        num -= (out[i]) * _pow(10, p);
    }
    return out[0]*1000 + out[1]*100 + out[2]*10 + out[3];
}

char kaprekar(short num){
    if(num == KAPREKAR_CONST) return 0;
    short big = desc_digits(num);
    short small = asc_digits(big);
    char count = 1;
    while(big - small != KAPREKAR_CONST){
        big = desc_digits(big - small);
        small = asc_digits(big);
        count++;
    }
    return count;
}

int main(int argc, char *argv[]){
    short num = (short) strtol(argv[1], NULL, 10);
    printf("largest_digit(%d) -> %d\n", num, largest_digit(num, NULL));
    printf("desc_digits(%d) -> %d\n", num, desc_digits(num));
    printf("kaprekar(%d) -> %d\n", num, kaprekar(num));
}
