/* 18/01/2017 */
#include <string.h>
#include <stdio.h>

unsigned char validSymbol(char *n, char *s){
    if(strlen(s) != 2) return 0;
    
    char name[50], symbol[3];
    strcpy(name, n);
    strcpy(symbol, s);
    name[0] += 32;              //making the first letter
    symbol[0] += 32;            //of each string lowercase;
    for(int i=0, index=0, flag; i < 2; i++){
        flag = 0;
        for(int j=index; j < strlen(name); j++){
            if(symbol[i] == name[j]){
                index = j+1;
                flag++;
                break;
            }
        }
        if(!flag)   return 0;
    }
    return 1;
}

int main(int argc, char* argv[]){
    printf("%s, %s -> %s\n", argv[1],
                             argv[2],
                             validSymbol(argv[1], argv[2]) ? "true" : "false");
}
