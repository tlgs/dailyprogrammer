# 29/05/2017

RULE = {'a': "bc", 'b': "a", 'c':"aaa"}

def collatz(value):
    print(value)
    if len(value) > 1:
        next_value = value[2:] + RULE[value[0]]
        return collatz(next_value)
    return