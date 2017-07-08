/* 08/07/2017 */
#include <stdio.h>
#include <time.h>
#include <stdlib.h>

int isVowel(char c){
    char vowels[5] = {'a', 'e', 'i', 'o', 'u'};
    for(int i=0; i < 5; i++){
        if(c == vowels[i]){
            return 1;
        }
    }
    return 0;
}

int main(int argc, char* argv[]){
    srand(time(0));
    char *ptr = argv[1];

    while(*ptr){
        char c = *ptr;
        int t = (c == 'C' || c == 'c') ? 1 : 0;
        do{
            c = rand()%26 + 'a';
        }while(isVowel(c) == t);
        putchar(c);
        ptr++;
    }
}