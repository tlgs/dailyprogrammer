/* 31/12/2016 */
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[]){
    int n = (int) strtol(argv[1], NULL, 10);

    for(int i = 1; i <= n; i++){
        if(i%3 == 0 && i%5 == 0){
            printf("FizzBuzz\n");
        }else if(i%3 == 0){
            printf("Fizz\n");
        }else if(i%5 == 0){
            printf("Buzz\n");
        }else{
            printf("%d\n", i);
        }
    }
}
