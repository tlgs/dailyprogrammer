/* 31/08/2017 */
#include <stdio.h>
#define SWAP(a, b) { (a)^=(b); (b)^=(a); (a)^=(b); }

int gcd(int a, int b){
    while (b != 0){
        a %= b;
        SWAP(a, b);
    }

    return a;
}

int main(void){
    int x, y, s;
    scanf("%d %d %d", &x, &y, &s);

    if(gcd(x, y) != 1){
        puts("no solution");
        return 0;
    }

    if (x > y)
       SWAP(x, y);
    
    int dx = 0, dy = 0, f = 0;
    while (dy != s){
        if (f)
            dx = 0;
        else{
            if (dx == x){
                f = !f;
                continue;
            }
            dy = y;
        }
        printf("(%d, %d)\n", dx, dy);

        int dc = dx;
        dx = dx+dy > x ? x : dx+dy;
        dy = dc+dy > x ? dy-(x-dc) : 0;
        printf("(%d, %d)\n", dx, dy);

        f = !f;
    }
}