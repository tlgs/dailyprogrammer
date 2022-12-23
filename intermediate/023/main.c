/* 10/02/2017 */
#include <stdio.h>
#include <stdlib.h>

void prt_not_mcn(int n){
    for(int i = 1; i <= n; i++){
        int d = i;
        while(d >= 0){
            if(d!=3 && (d>43 || d%3==0)) break;
            d -=20;
        }
        if(d < 0) printf("%d\n", i);
    }
}

int main(int argc, char* argv[]){
    int n = strtol(argv[1], NULL, 10);
    prt_not_mcn(n);
    return 0;
}
