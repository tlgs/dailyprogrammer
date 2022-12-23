# 07/04/2017

def create_possibles(x):
    l = [x]
    f = lambda x: [x.replace('*', '_'*n, 1) for n in range(0, 5)]

    for char in range(0, len(x) + x.count('*')*3):
        for string in l:
            try:
                if string[char] == '*':
                    l.extend(f(string))
            except:
                continue

    return [item for item in set(l) if '*' not in item]

def check_eq(a, b):
    if(len(a) != len(b)):
        return False
    for x, y in zip(a, b):
        if x != '_' and y != '_' and x!=y:
            return False
    return True

def overlap(a, b):
    a, b = create_possibles(a), create_possibles(b)
    for i in a:
        for j in b:
            if check_eq(i, j):
                return True
    return False
