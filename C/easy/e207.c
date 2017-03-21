/* 21/03/2017 */
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

char * getComplement(char *in, int size){
    char *out = malloc(sizeof(char) * size);
    for(int i = 0; i < size-1; i++){
        switch(in[i]){
            case 'A': out[i] = 'T';
                      break;
            case 'T': out[i] = 'A';
                      break;
            case 'G': out[i] = 'C';
                      break;
            case 'C': out[i] = 'G';
                      break;
            default:  out[i] = ' ';
        }
    }
    out[size-1] = '\0';
    return out;
}

int main(int argc, char *argv[]){
    int size = strlen(argv[1]) + 1;
    char *input = malloc(sizeof(char) * size);
    strcpy(input, argv[1]);

    char *output = malloc(sizeof(char) * size);
    output = getComplement(input, size);
    printf("%s\n%s", input, output);
}
