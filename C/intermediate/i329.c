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
    
    int dx = 0, dy = 0, c = 0;
    while (dy != s){
        if (dx == x)
            dx = 0;
        else
            dy = y;
        printf("(%d, %d)\n", dx, dy);

        int dc = dx;
        dx = dx+dy > x ? x : dx+dy;
        dy = dc+dy > x ? dy-(x-dc) : 0;
        printf("(%d, %d)\n", dx, dy);
        c+=2;
    }
    printf("steps: %d", c);
}