/* 12/07/2017 */
#include <stdlib.h>
#include <stdio.h>

#define MAXTUPLES 1024*4

int cmpInt(const void * a, const void * b)
{
   return ( *(int*)a - *(int*)b );
}

int main(int argc, char* argv[]){
    // parse list of integers
    int n = argc-1;
    int *v = malloc(sizeof(int) * n);
    for (int i=0; i < n; i++){
        v[i] = strtol(argv[i+1], NULL, 10);
    }

    // https://en.wikipedia.org/wiki/3SUM#Quadratic_algorithm
    // with a slight change to avoid repeating tuples
    int found[MAXTUPLES][3];
    unsigned int count = 0;

    qsort(v, n, sizeof(int), cmpInt);
    for (int i=0; i < n-3; i++){
        int a = v[i];
        int start = i+1;
        int end = n-1;
        while (start < end){
            int b = v[start];
            int c = v[end];
            if (a+b+c == 0){
                char flag = 0;
                for (int j = count-1; j >= 0; j--){
                    if (found[j][0] == a && found[j][1] == b && found[j][2] == c){
                        flag = 1;
                        break;
                    }
                }
                if (!flag){
                    found[count][0] = a;
                    found[count][1] = b;
                    found[count][2] = c;
                    count++;
                    printf("(%d, %d, %d)\n", a, b, c);
                }
                end--;
            }
            else if (a+b+c > 0){
                end--;
            }
            else{
                start++;
            }
        }
    }
    return 0;
}