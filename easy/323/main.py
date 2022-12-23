# 10/07/2017
from itertools import combinations

three_sum = lambda l: print('\n'.join({str(sorted(t)) for t in combinations(l, 3) if sum(t) == 0}))
