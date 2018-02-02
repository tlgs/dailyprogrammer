/* 02/02/2018 */
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define LIFESPAN 8*12
#define FERTILE_START 4
#define MALE_OFFSPRING 5
#define FEMALE_OFFSPRING 9

int main(int argc, char* argv[]){
    unsigned long long male[LIFESPAN] = {0};
    unsigned long long female[LIFESPAN] = {0};
    unsigned long long goal = strtoll(argv[3], NULL, 10);
    int months = 0;

    male[2] = strtoll(argv[1], NULL, 0);
    female[2] = strtoll(argv[2], NULL, 0);
    
   while(1) {
        unsigned long long fertile = 0;
        for (int i = FERTILE_START; i < LIFESPAN; i++)
            fertile += female[i];

        memmove(male+1, male, sizeof(*male) * (LIFESPAN-1));
        memmove(female+1, female, sizeof(*female) * (LIFESPAN-1));

        male[0] = MALE_OFFSPRING * fertile;
        female[0] = FEMALE_OFFSPRING * fertile;

        months++;
        unsigned long long total = 0;
        for (int i=0; i < LIFESPAN; i++)
            total += male[i] + female[i];
        if (total >= goal)
            break;
    }
    
    printf("%d", months);
}