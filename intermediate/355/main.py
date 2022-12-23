# 15/04/2018
import random

def bake(ingredients):
    '''Hello Mr. Hill Climber'''
    recipes = [[1, 0], [0, 1], [3, 4], [4, 3], [3, 2]]
    best = [0, 0]
    for _ in range(1000):  # edit for more iterations
        curr = [0, 0]
        while all([curr[0]*A[0] + curr[1]*A[1] <= b for A, b in zip(recipes, ingredients)]):
            if sum(curr) > sum(best):
                best = curr[:]
            curr[random.randint(0, 1)] += 1

    return best
