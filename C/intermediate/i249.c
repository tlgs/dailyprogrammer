/* 01/03/2017 */
/* Currently takes about ~1500 generations to get "Hello, World!" using this parameters.
** Uses one-point crossover.
** Fitness-proportional selection for parent selection.
** Fitness-proportional selection to decide next generation (parents + children).
**
** Does not converge properly:
** [Can make the mutation probability decrease with time]
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define POP_SIZE 200
#define CHILDREN_NUM 300
#define PARENT_NUM 100

#define LAMBDA 0.5
#define P_MUTATE 0.01

typedef struct {
    char *solution;
    int fitness;
} individual;

typedef struct {
    individual population[POP_SIZE];
    int no;
} gen;

gen initPop(char *target);
gen nextGen(gen input, char *target);
void printHeader(int gen, individual input);

int fitnessFunction(char *test, char *target);
void evaluatePop(individual *input, char *target, int size);
individual getBest(individual *input);

void selectParents(individual *input, individual *parents);
void createChildren(individual *parents, individual *children);
void mutatePop(individual *input, int size);
void selectNextPop(individual *parents, individual *children, individual *new);

void printPop(individual *input, int size);
void freePop(individual *parents, individual *children, individual *next);

int main(int argc, char *argv[]){
    int targetSize = strlen(argv[1]);
    char *target = (char *) malloc(sizeof(char) * targetSize);
    strcpy(target, argv[1]);

    srand(time(0));
    gen generation = initPop(target);
    printHeader(generation.no, getBest(generation.population));

    while(strcmp(getBest(generation.population).solution, target) != 0){
        generation = nextGen(generation, target);
        printHeader(generation.no, getBest(generation.population));
    }
}

gen initPop(char *target){
    int size = strlen(target);
    gen output;
    output.no = 1;
    for(int number = 0; number < POP_SIZE; number++){
        output.population[number].fitness = 0;
        output.population[number].solution = (char *) malloc(sizeof(char) * (size + 1));
        for(int chr = 0; chr <= size; chr++){
            output.population[number].solution[chr] = (chr == size) ? 0 : 32 + rand() % 95;
        }
    }
    evaluatePop(output.population, target, POP_SIZE);
    return output;
}

gen nextGen(gen input, char *target){
    individual *parents = malloc(sizeof(individual) * PARENT_NUM);
    selectParents(input.population, parents);

    individual *children = malloc(sizeof(individual) * CHILDREN_NUM);
    createChildren(parents, children);
    mutatePop(children, CHILDREN_NUM);
    evaluatePop(children, target, CHILDREN_NUM);

    individual *nextPop = malloc(sizeof(individual) * (CHILDREN_NUM+PARENT_NUM));
    selectNextPop(parents, children, nextPop);

    int targetSize = strlen(children[0].solution);
    gen output;
    output.no = input.no + 1;
    for(int number = 0; number < POP_SIZE; number++){
        output.population[number].fitness = 0;
        output.population[number].solution = (char *) malloc(sizeof(char) * (targetSize + 1));
        strcpy(output.population[number].solution, nextPop[number].solution);
    }

    freePop(parents, children, nextPop);
    evaluatePop(output.population, target, POP_SIZE);
    return output;
}

void printHeader(int gen, individual input){
    printf("gen: %3d  | %s | %d\n", gen, input.solution, input.fitness);
}

int fitnessFunction(char *test, char *target){
    int sum = 0;
    for(int chr = 0; chr < strlen(target); chr++){
        if(!(target[chr] - test[chr])){
            sum += 1;
        }
    }
    return sum;
}

void evaluatePop(individual *input, char *target, int size){
    for(int i = 0; i < size; i++){
        input[i].fitness = fitnessFunction(input[i].solution, target);
    }
}

individual getBest(individual *input){
    int index = 0;
    int best = input[0].fitness;
    for(int i = 0; i < POP_SIZE; i++){
        if(input[i].fitness > best){
            index = i;
            best = input[i].fitness;
        }
    }
    return (individual) {input[index].solution, input[index].fitness};
}

void selectParents(individual *input, individual *parents){
    int probabilities[POP_SIZE];
    int sum = 0;
    for(int i = 0; i < POP_SIZE; i++){
        probabilities[i] = input[i].fitness + sum;
        sum += input[i].fitness;
    }

    int targetSize = strlen(parents[0].solution);
    for(int i = 0; i < PARENT_NUM; i++){
        int dice = rand()%probabilities[POP_SIZE-1];
        for(int j = 0; j < POP_SIZE; j++){
            if(dice < probabilities[j]){
                parents[i].solution = malloc(sizeof(char) * (targetSize + 1));
                strcpy(parents[i].solution, input[j].solution);
                parents[i].fitness = input[j].fitness;
                break;
            }
        }
    }
}

void createChildren(individual *parents, individual *children){
    int size = strlen(parents[0].solution);
    if(CHILDREN_NUM % 2){
        printf("Children number must be even!\n");
        return;
    }

    for(int i = 0; i < CHILDREN_NUM; i += 2){
        int pOne = rand() % PARENT_NUM;
        int pTwo = rand() % PARENT_NUM;
        children[i].solution = malloc(sizeof(char) * (size + 1));
        children[i + 1].solution = malloc(sizeof(char) * (size + 1));
        for(int j = 0; j < size; j++){
            children[i + (j >= LAMBDA*size)].solution[j] = parents[pOne].solution[j];
            children[i + (j < LAMBDA*size)].solution[j] = parents[pTwo].solution[j];

        }
        children[i].solution[size] = '\0';
        children[i + 1].solution[size] = '\0';

        children[i].fitness = 0;
        children[i + 1].fitness = 0;
    }
}

void mutatePop(individual *input, int size){
    for(int i = 0; i < size; i++){
        for(int j = 0; j < strlen(input[0].solution); j++){
            if(rand()%100 < P_MUTATE * 100)
                input[i].solution[j] = 32 + rand() % 95;
        }
    }
}

void selectNextPop(individual *parents, individual *children, individual *new){
    int probabilities[PARENT_NUM + CHILDREN_NUM];
    int sum = 0;
    for(int i = 0; i < PARENT_NUM + CHILDREN_NUM; i++){
        probabilities[i] = (i < PARENT_NUM) ? parents[i].fitness + sum :
                                              children[i - PARENT_NUM].fitness + sum;
        sum += (i < PARENT_NUM) ? parents[i].fitness : children[i - PARENT_NUM].fitness;
    }

    int targetSize = strlen(parents[0].solution);
    for(int i = 0; i < POP_SIZE; i++){
        int dice = rand() % probabilities[PARENT_NUM + CHILDREN_NUM - 1];
        for(int j = 0; j < PARENT_NUM + CHILDREN_NUM; j++){
            if(dice < probabilities[j]){
                new[i].solution = malloc(sizeof(char) * (targetSize + 1));
                strcpy(new[i].solution, (j < PARENT_NUM) ? parents[j].solution :
                                                           children[j - PARENT_NUM].solution);
                new[i].fitness = (j < PARENT_NUM) ? parents[j].fitness : children[j - PARENT_NUM].fitness;
                break;
            }
        }
    }
}

void printPop(individual *input, int size){
    for(int i = 0; i < size; i++){
        printf("%3d:\t%s\t%2d\n", i, input[i].solution, input[i].fitness);
    }
}

void freePop(individual *parents, individual *children, individual *next){
    for(int i = 0; i < PARENT_NUM; i++){
        free(parents[i].solution);
    }
    free(parents);

    for(int i = 0; i < CHILDREN_NUM; i++){
        free(children[i].solution);
    }
    free(children);

    for(int i = 0; i < POP_SIZE; i++){
        free(next[i].solution);
    }
    free(next);
}
