/* 07/01/2017 */
#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <string.h>

int main(){
    system("CLS");      //clear screen
    srand(time(NULL));  //set rand seed
    int n = rand() % 100 + 1;
    char answer[10];
    printf("\nConsole: Welcome to Guess-that-number game. I have picked a number in [1, 100]. Please make a guess.\nUser: ");
    fgets(answer, 10, stdin);
    answer[strlen(answer) - 1] = '\0';  //dealing with the extra '\n'

    while(strtol(answer, NULL, 10) != n){
        if(strcmp(answer, "exit") == 0){
            printf("Console: <Program terminates>");
            return 0;
        }else if(strtol(answer, NULL, 10) == 0L){   //is the case when it can't convert properly
            printf("Console: Wrong. That is not a number.\n");
        }else if(strtol(answer, NULL, 10) > n){
            printf("Console: Wrong. That number is above my number.\n");
        }else{
            printf("Console: Wrong. That number is below my number.\n");
        }

        printf("User: ");
        fgets(answer, 10, stdin);
        answer[strlen(answer) - 1] = '\0';  //dealing with the extra '\n'
    }

    printf("Console: Correct! That is my number! <Program terminates>");
}
