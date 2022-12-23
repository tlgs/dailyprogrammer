# 05/03/2018
# brute-forced with combinations within a range constructed from the constraints
import sys
from itertools import combinations

goal, coins = sys.stdin.readline().split(maxsplit=2)[1:]
constraint, n = sys.stdin.readline().split(maxsplit=4)[2:]
coins, goal, n = list(map(int, coins.split())), int(goal), int(n)
rule = {'>': (n+1, len(coins)), '>=': (n, len(coins)), '<':(1, n-1), '<=':(1, n)}[constraint]

solution = []
for i in range(rule[0], rule[1]+1):
    solution += [str(c) for c in combinations(coins, i) if sum(c) == goal]
print('\n'.join(solution) if solution else "no solution")
