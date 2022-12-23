/* 01/01/2017 */
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[]){
    int n = (int) strtol(argv[1], NULL, 10);
    while(n != 1){
        switch(n%3){
            case 0: printf("%d 0\n", n);
                    break;
            case 1: printf("%d -1\n", n--);
                    break;
            case 2: printf("%d +1\n", n++);
        }
        n /= 3;
    }
    printf("%d", n); 
}
