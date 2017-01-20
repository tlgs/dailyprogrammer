/* 20/01/2017 */
#include <stdio.h>

float p(int d, int h){
    if(h > d)
        return (1 / (float) d) * p(d, h-d);
    else
        return (1 / (float) d * (d-h+1));
}

int main(void){
    int input[][2] = {{4,1}, {4,4}, {4,5}, {4,6}, {1,10}, {100, 200}, {8,20}};
    for(int i=0; i < 7; i++)
        printf("%3d : %3d  -->   %0.5f\n", input[i][0], input[i][1], p(input[i][0], input[i][1]));
}
