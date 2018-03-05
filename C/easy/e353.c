/* 05/03/2018 */
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

struct seq {
    char value[32];
    unsigned short distance; 
};

unsigned short hamming (char a[], char b[]){
    unsigned short total = 0;
    for (int i = 0; i < strlen(a); i++)
        total += (a[i] != b[i]);
    return total;
}

int cmp (const void *a, const void *b){
    struct seq *seqA = (struct seq *) a;
    struct seq *seqB = (struct seq *) b;
    return seqA->distance - seqB->distance;
}

int main (void){
    unsigned short n;
    scanf("%d", &n);
    struct seq *arr = malloc(sizeof(struct seq) * n);
    for (int i = 0; i < n; i++){
        scanf("%s", arr[i].value);
        arr[i].distance = 0;
        for (int j = 0; j < i; j++){
            unsigned short diff = hamming(arr[i].value, arr[j].value);
            arr[i].distance += diff;
            arr[j].distance += diff;
        }
    }
    qsort(arr, n, sizeof(struct seq), cmp);
    puts(arr[0].value);
}