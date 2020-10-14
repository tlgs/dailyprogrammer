# 14/10/2020

import random


def bogo(s, t):
    s, t = map(list, [s, t])
    count = 0
    while s != t:
        random.shuffle(s)
        count += 1

    return count
