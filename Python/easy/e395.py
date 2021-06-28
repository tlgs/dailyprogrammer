# 22/06/2021
import itertools


def nonogramrow(seq):
    return [sum(g) for k, g in itertools.groupby(seq) if k]


assert nonogramrow([]) == []
assert nonogramrow([0, 0, 0, 0, 0]) == []
assert nonogramrow([1, 1, 1, 1, 1]) == [5]
assert nonogramrow([0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1]) == [5, 4]
assert nonogramrow([1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0]) == [2, 1, 3]
assert nonogramrow([0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1]) == [2, 1, 3]
assert nonogramrow([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == [
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
]
