/* 30/11/2017 */
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX_SIZE 1024
#define MAX_CHARS 16

int alreadySeen(char** list, int size, char* curr){
    for (int i = 0; i < size; i++){
        if (strcmp(list[i], curr) == 0)
            return 1;
    }
    return 0;
}

int main(int argc, char* argv[]){
    char **list = malloc(sizeof(char)*MAX_SIZE*MAX_CHARS);
    int listCount = 0;

    int size = strlen(argv[1]);
    for (int target = 2; target < size; target++){
        for (int pos = 0; pos < size-target; pos++){
            char* curr = malloc(sizeof(char) * target + 1);
            strncpy(curr, argv[1] + pos, target);
            curr[target] = '\0';
            if(alreadySeen(list, listCount, curr))
                continue;

            int count = 1;
            for (int i = pos+1; i < size-target+1; i++){
                char* test = malloc(sizeof(char) * target + 1);
                strncpy(test, argv[1] + i, target);
                test[target] = '\0';
                if (strcmp(curr, test) == 0)
                    count++;
            }
            if (count > 1)
                printf("%s: %d\n", curr, count);

            list[listCount] = malloc(sizeof(char)*MAX_CHARS);
            strcpy(list[listCount], curr);
            listCount++;
        }
    }
}