# 28/07/2017

def unique_factors(x):
    factors = set()
    for div in range(2, x+1):
        while(x % div == 0):
            x /= div
            factors |= {div}

    return factors

def is_ruth_aaron(pair):
    return len(set([sum(unique_factors(x)) for x in pair])) == 1