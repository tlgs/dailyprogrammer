# 15/03/2017
from itertools import starmap

def gray_code_seq(n):
    if n == 1:
        return [0, 1]
    else:
        f = lambda x, p: '{:{pre}>{width}}'.format(x, pre=p, width=n)
        to_list = lambda x, p: list(starmap(f, zip(x, [p]*2**(n-1))))
        return to_list(gray_code_seq(n-1), 0) + to_list(gray_code_seq(n-1)[::-1], 1)
