# 08/01/2019
# based on u/Lopsidation solution


def qcheck(rows):
    def distinct(r):
        return len(r) == len(set(r))

    down = [x + i for i, x in enumerate(rows)]
    up = [x - i for i, x in enumerate(rows)]

    return(distinct(rows) and distinct(down) and distinct(up))

assert qcheck([2, 4, 6, 1, 3, 5]) is True
assert qcheck([4, 2, 7, 3, 6, 8, 5, 1]) is True
assert qcheck([2, 5, 7, 4, 1, 8, 6, 3]) is True
assert qcheck([5, 3, 1, 4, 2, 8, 6, 3]) is False
assert qcheck([5, 8, 2, 4, 7, 1, 3, 6]) is False
assert qcheck([4, 3, 1, 8, 1, 3, 5, 2]) is False
