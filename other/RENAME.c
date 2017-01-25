/*
** This piece of code was used to rename
** all solution files from easyXXX -> eXXX
*/
#include <stdio.h>
#include <unistd.h>

#define MAXFILES 300
#define EXTENSION ""

int main(void){
    for(int i = 0; i < MAXFILES; i++){
        char old[256], new[256];
        snprintf(old, sizeof(old), "%s%03d%s", "easy", i, EXTENSION);
        if(access(old, F_OK) != -1){
            snprintf(new, sizeof(new), "%s%03d%s", "e", i, EXTENSION);
            rename(old, new);
        }
    }
}
