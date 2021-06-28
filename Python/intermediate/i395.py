import functools


@functools.lru_cache(maxsize=None)
def phonedrop(n, h):
    if 1 in (n, h):
        return h

    worst = 0
    for i in range(1, h):
        x = phonedrop(n - 1, i) + 1
        y = phonedrop(n, h - i) + 1
        worst = max(worst, min(x, y))

    return worst


assert phonedrop(1, 100) == 100
assert phonedrop(2, 100) == 14
assert phonedrop(3, 100) == 9
assert phonedrop(1, 1) == 1
assert phonedrop(2, 456) == 30
assert phonedrop(3, 456) == 14
assert phonedrop(4, 456) == 11
assert phonedrop(2, 789) == 40
assert phonedrop(3, 789) == 17
assert phonedrop(4, 789) == 12
