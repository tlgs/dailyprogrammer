/* 20/01/2017 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

char * encodeMatrix(char *text, int key);
char * decodeMatrix(char *text, int key);

int main(int argc, char* argv[]){
    srand(time(NULL));
    int key = (int) strtol(argv[2], NULL, 10);
    char encoded[256];
    strcpy(encoded, encodeMatrix(argv[1], key));
    puts(encoded);
    puts(decodeMatrix(encoded, key));
}

char * encodeMatrix(char *text, int key){
    const int size = strlen(text);
    char *output = malloc(sizeof(char) * (size + size%key));
    for(int i=0, c=0; i < key; i++){
        for(int j=0; j < size/key + (size%key > 0); j++){
            if(i + j*key >= size)
                output[c++] = 97 + rand()%26;
            else
                output[c++] = text[i + j*key];
        }
    }
    output[size + size%key] = '\0';
    return output;
}

char * decodeMatrix(char *text, int key){
    const int size = strlen(text);
    char *output = malloc(sizeof(char) * strlen(text));
    for(int i=0, c = 0; i < size/key; i++){
        for(int j=0; j < key; j++){
            output[c++] = text[i + j*(size/key)];
        }
    }
    output[size] = '\0';
    return output;
}
