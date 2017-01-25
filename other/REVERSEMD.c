/*
** This piece of code was used to
** reverse a markdown table
*/
#include <stdlib.h>
#include <stdio.h>

#define MAXSTREAM 1024
#define TABLESTART 13
#define MAXTABLE 400

int main (void){
    FILE *fi, *fo;
    char ignore[MAXSTREAM];

    fi = fopen("../README.md", "r");
    for(char i = 0; i < TABLESTART; i++)
        fgets(ignore, MAXSTREAM, fi);

    char **index = (char**) malloc(sizeof(char) * MAXTABLE);
    int line = 0;
    do {
        index[line] = (char*) malloc(sizeof(char) * MAXSTREAM);
    } while(fgets(index[line++], MAXSTREAM, fi));
    fclose(fi);

    fo = fopen("reversed.txt", "w");
    for(int i = line - 2; i >= 0; i--){
        fprintf(fo, "%s", index[i]);
    }
    fclose(fo);
}
