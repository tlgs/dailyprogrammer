/* 18/06/2017 */
#include <stdio.h>
#define fumble(d)  (*d*2 + *(d+1) - 250)

int eng_to_dec(char* digit){
    char decode[] = "_ReVA;UQ9K";
    for (int i=0; i<10; i++){
        if(fumble(digit) == decode[i]){
            return i;
        }
    }
}

int main(void){
    char * test[] = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};

    for (int i=0; i < 10; i++){
        printf("eng_to_dec(\'%s\') #\t => %d\n", test[i], eng_to_dec(test[i]));
    }
}