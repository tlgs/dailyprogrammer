/* 12/06/2017 */
#include <stdio.h>
#include <stdlib.h>

struct Purse {
    unsigned int quarters;
    unsigned int dimes;
    unsigned int nickels;
    unsigned int pennies;
};

struct Purse findMinimumCoins(float value){
    struct Purse purse = {.quarters = 0, .dimes = 0, .nickels = 0, .pennies = 0};
    unsigned char curr = 0;
    float coinValues[4] = {0.25, 0.10, 0.5, 0.01};
    while(value >= 0.01){
        for(; value < coinValues[curr]; curr++);
        switch(curr){
            case 0: purse.quarters++; break;
            case 1: purse.dimes++; break;
            case 2: purse.nickels++; break;
            case 3: purse.pennies++; break;
        }
        value -= coinValues[curr];
    }
    
    return purse;
}

int main(int argc, char* argv[]){
    float value = strtof(argv[1], NULL);
    struct Purse min = findMinimumCoins(value);
    printf("Quarters: %d\nDimes: %d\nNickels: %d\nPennies: %d\n", 
            min.quarters, min.dimes, min.nickels, min.pennies);
}
