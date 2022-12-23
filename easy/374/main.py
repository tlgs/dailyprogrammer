# 29/01/2019


def additive_persistence(n, i=0):
    if n < 10:
        return i
    s = 0
    while n != 0:
        n, s = map(sum, zip(divmod(n, 10), (0, s)))
    return additive_persistence(s, i+1)

assert additive_persistence(13) == 1
assert additive_persistence(1234) == 2
assert additive_persistence(9876) == 2
assert additive_persistence(199) == 3
