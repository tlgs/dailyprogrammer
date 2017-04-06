# 09/03/2017
from scipy.special import comb

def pascal_number(x, y):
    print('Input: {}, {}'.format(x, y))
    print('Error') if y > x+1 else print('Output: {}'.format(comb(x-1, y-1, exact=True)))

def print_pascal_triangle(n=15):
    f = lambda x: ' '.join([str(comb(x, index, exact=True)) for index in range(0, x+1)])
    for line in range(0, n):
        print('{str:^{width}}'.format(str=f(line), width=len(f(n-1))))
