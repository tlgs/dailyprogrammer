/* 01/01/2016 */
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

#define MAXBUFFER 128

int isVowel(char ch){
    if(ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u')
        return 1;
    else
        return 0;
}

int main(){
    char *line = (char*) calloc(MAXBUFFER, sizeof(char));
    char *outConsonants = (char*) calloc(MAXBUFFER, sizeof(char));
    char *outVowels = (char*) calloc(MAXBUFFER, sizeof(char));
    int c = 0, v = 0;

    fgets(line, MAXBUFFER, stdin);
    for(int i = 0; i < strlen(line); i++){
        if(isVowel(line[i]))
            outVowels[v++] = line[i];
        else if(isalpha(line[i]))
            outConsonants[c++] = line[i];
    }

    printf("%s\n%s", outConsonants, outVowels);
}
