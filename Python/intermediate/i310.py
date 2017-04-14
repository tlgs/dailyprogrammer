# 14/04/2016
from math import floor, sqrt, gcd

def simplify_rad(b):
    a = 1
    sq_factors = lambda n: [f for f in range(2, floor(sqrt(n))+1) if not n%f**2]
    for f in sq_factors(b)[::-1]:
        while not b % f**2:
            a *= f
            b //= f**2
    return a, b

def simplify_frac(a, b, c, d):
    a, b = tuple(x*y for x, y in zip((a, 1), simplify_rad(b*d)))
    div = gcd(a, c*d)
    a //= div
    c = c*d // div
    return a, b, c
