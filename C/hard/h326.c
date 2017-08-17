/* 14/08/2017 */
/* usage: .\a < real_words.txt */
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

#define MAX_WLENGTH 32
#define MAX_WCOUNT 1024*1024

int cmpChar(const void * a, const void * b);
int find(char blocks[], int N,  char c, int start);
int contains(char blocks[], int N, char word[]);
int validate(char blocks[], int N, char words[][MAX_WLENGTH], int size);

int main(void){
    static char words[MAX_WCOUNT][MAX_WLENGTH];
    unsigned int nwords = 0;
    char line[MAX_WLENGTH];
    while (fgets(line, sizeof(line), stdin)){
        line[strlen(line)-1] = '\0';
        strcpy(words[nwords++], line);
    }

    /* Starting from a known solution */
    char start[] = "ehiaoslnrtaeiotcdnorsacegioucdgilmpsehilmnosubdglmnpstvbefghinprsyafghklpuvwxzabcdgjkqrtwxyadefjklnpqruyz";
    int N = 14;

    char best[N*(N+1)/2];
    strcpy(best, start);
    unsigned char improve;
    do{
        improve = 0;
        for (int i = 0; i < N*(N+1)/2; i++){
            char attempt[N*(N+1)/2];
            strcpy(attempt, best);

            for (int j = 97; j < best[i]; j++){
                attempt[i] = j;
                if (validate(attempt, N, words, nwords)){
                    strcpy(best, attempt);
                    improve = 1;
                    break;
                }
            }
        }
    }
    while (improve);

    for (int i = 0; i < N; i++)
        qsort(best + i*(i+1)/2, i+1, sizeof(char), cmpChar);

    puts(best);
}


int cmpChar(const void* a, const void* b){
    return *(char*)a - *(char*)b;
}

int find(char blocks[], int N,  char c, int start){
    for (int i = start; i < N; i++){
        for (int j = 0; j <= i; j++){
            if (blocks[i*(i+1)/2 + j] == c)
                return i;
        }
    }
    return -1;
}

int contains(char blocks[], int N, char word[]){
    char stack[64];
    int top = 0;
    int popped = -1;
    unsigned long used = 0;

    do{
        for (int j = top; j < strlen(word); j++){
            int nxt = find(blocks, N, word[j], popped + 1);
            popped = -1;

            while (used & (1 << nxt))
                nxt = find(blocks, N, word[j], nxt + 1);
            
            if (nxt == -1)
                break;

            stack[++top] = nxt;
            used |= (1ul << nxt);
        }

        if (__builtin_popcount(used) == strlen(word))
            return 1;
            
        popped = stack[top--];
        used &= ~(1ul << popped);
    }
    while (top > -1);

    return 0;
}

int validate(char blocks[], int N, char words[][MAX_WLENGTH], int size){
    int flag = 1;
    for (int i = 0; i < size; i++){
        if(!contains(blocks, N, words[i])){
            //puts(words[i]);
            flag = 0;
            break;
        }  
    }
    return flag;
}