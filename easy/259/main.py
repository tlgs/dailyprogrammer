# 22/03/2017
from math import sqrt

def typing_dist(addr):
    last = ['.', 0]
    coord = lambda num: (last.index(num) if num in last else (int(num) - 1) % 3,
                         3 if num in last else int( (int(num) - 1) / 3) )

    dist = lambda a, b: sqrt(abs(coord(a)[0]-coord(b)[0])**2 +
                             abs(coord(a)[1]-coord(b)[1])**2)

    return "{:.2f}cm".format(sum([dist(a, b) for a, b in zip(addr, addr[1:])]))
