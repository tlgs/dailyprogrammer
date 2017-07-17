/* 17/07/2017 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define LINE_SIZE 32

int cmpStrLen(const void * a, const void * b){
   return ( strlen((char*)a) - strlen((char*)b) );
}

int main(int argc, char **argv){
    FILE *f;
    f = fopen("..\\..\\other\\enable1.txt", "r");
    char words[1024][LINE_SIZE];
    int count = 0;

    char line[LINE_SIZE];
    while(fgets(line, LINE_SIZE, f)){
        if(line[0] == 'a' && line[1] == 't'){
            line[strlen(line)-1] = '\0';
            strcpy(words[count], line);
            count++;
        }
    }

    qsort(words, count, sizeof(char)*LINE_SIZE, cmpStrLen);
    for(int i = 0; i < 20; i++){
        if(i == 10)
            putchar('\n');

        char out[LINE_SIZE*2] = "@";
        char original[LINE_SIZE];
        strcpy(original, words[(i/10) ? i-10 : count-1-i]);

        strcpy(out+1, original+2);
        strcat(out, " : ");
        strcat(out, original);

        puts(out);
    }

    return 0;
}