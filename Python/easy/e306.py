# 13/03/2017
from roman import fromRoman
from itertools import permutations

def find_pandigital_romans(n=2000):
    f = permutations
    l = [''.join(('M',) + i + j + k) for i in f('CD', 2) for j in f('XL', 2) for k in f('IV', 2)]
    print(*list(map(fromRoman, l)), sep='\n')
