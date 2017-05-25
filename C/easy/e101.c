/* 25/05/2017 */

#include <stdio.h>

int main(void){
    unsigned short begin, end;
    while(scanf("%hu %hu", &begin, &end) == 2){
        unsigned short counter = 0;
        for(unsigned short i = begin; i <= end; i++){
            /* assume 4-digit years */
            char a = i%10;
            char b = (i/10)%10;
            char c = (i/100)%10;
            char d = i/1000;
            if(!(a == b || a == c || a == d || b == c || b == d || c == d))
                counter++;   
        }
        printf("There are %hu non-repeating years between %hu and %hu.\n", counter, begin, end);
    }
}