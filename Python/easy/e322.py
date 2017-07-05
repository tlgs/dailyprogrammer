# 05/07/2017
from itertools import product, combinations
from math import factorial

def all_pairs_gen(iterable):
    n = len(iterable)
    all_combinations = [set(x) for x in product(*iterable)]
    output = []
    for threshold in range(factorial(n) // 2 * factorial(n-2), 0, -1):
        for member in all_combinations:
            if sum([all([not set(x).issubset(s) for s in output]) for x in combinations(member, 2)]) >= threshold:
                output.append(member)

    output = sorted([str(sorted(x)) for x in output])
    return output