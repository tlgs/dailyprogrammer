/* 13/10/2017 */
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int _pow(int a, int b){
    return b == 0 ? 1 : a * _pow(a, b-1);
}

int _index(int i, int n){
    if (n == 1)
        return i;
    else{
        int sq = (i / _pow(3, 2*n-1)) * 3 + (i % _pow(3, n) / _pow(3, n-1));
        int next = i - (i / _pow(3, n) * _pow(3, n-1) * 2 + i % _pow(3, n) / _pow(3, n-1) * _pow(3, n-1) + sq/3 * _pow(9, n-1));                
        return sq * _pow(9, n-1) + _index(next, n-1);
    }
}

int main(void){
    int ncolors, niterations;
    scanf("%d %d", &ncolors, &niterations);
    int rules[ncolors][9];
    for (int i=0; i < ncolors; i++)
        for (int j=0; j < 9; j++)
            scanf("%d", &rules[i][j]);

    int *canvas = calloc(sizeof(int), _pow(_pow(3, niterations), 2));
    for (int i=1; i <= niterations; i++){
        int new[_pow(_pow(3, i), 2)];
        for (int j=0; j < _pow(_pow(3, i-1), 2); j++)
            for (int k=0; k < 9; k++)
                new[j*9+k] = rules[canvas[j]][k];
                
        memcpy(canvas, new, sizeof(int)*_pow(_pow(3, i), 2));
    }

    printf("P2\n%d %d\n%d\n", _pow(3, niterations), _pow(3, niterations), ncolors-1);
    for (int i=0; i < _pow(_pow(3, niterations), 2); i++)
        printf("%d%c", canvas[_index(i, niterations)], i % _pow(3, niterations) == 0 && i > 0 ? '\n' : 32);
}