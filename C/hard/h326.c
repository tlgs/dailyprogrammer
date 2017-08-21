/* 14/08/2017 */
/* usage: .\a < real_words.txt */
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

#define MAX_WLENGTH 32

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

int main(void){
   return 0;
}