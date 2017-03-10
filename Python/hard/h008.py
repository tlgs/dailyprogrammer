# 09/03/2017
from scipy.special import comb

def pascalNumber(x, y):
    print('Input: {}, {}'.format(x, y))
    print('Error') if y > x+1 else print('Output: {}'.format(comb(x-1, y-1, exact=True)))

def printPascalTriangle(n=15):
    for line in range(0, n):
        t = ' '.join([str(comb(line, index, exact=True)) for index in range(0, line+1)])
        print('{str:^{width}}'.format(str=t, width=(n-1) * 2 + 1))
