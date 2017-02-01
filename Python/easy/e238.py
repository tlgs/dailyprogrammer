# 31/01/2017
import random

def replace_vc(x):
    if x in 'vV':
        y = "aeiou"[random.randint(0, 4)]
    elif x in 'cC':
        y = "bcdfghjklmnpqrstvwxyz"[random.randint(0, 20)]
    return y if x.islower() else y.upper()

def create_word(pattern):
    if len([x for x in pattern if x in 'cCvV']) != len(pattern):
        return "Input should only consist of 'c's and 'v's"
    return ''.join(list(map(replace_vc, pattern)))
