# 14/01/2018
from itertools import permutations
import time

def cryptarithmetic_solver(puzzle):
    '''
    Solves cryptarithms using brute-force.
    Notes: eval() is frowned upon + direct translation is very expensive.
    '''
    start = time.perf_counter()
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    leading = list(set(c[0] for c in puzzle.split() if c[0] in alphabet))
    letters = list(set([c for c in puzzle if c in alphabet]))
    for attempt in permutations("0123456789", len(letters)):
        attempt = {k: v for k, v in zip(letters, attempt)}
        if any([attempt[k] == '0' for k in leading]):
            continue
        elif eval(''.join([attempt[k] if k in letters else k for k in puzzle])):
            print("Time taken: {:.2f} seconds".format(time.perf_counter() - start))
            return '{' + ', '.join(sorted(['"{}"=>{}'.format(k, attempt[k]) for k in attempt])) + '}'
