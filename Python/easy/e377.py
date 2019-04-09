# 09/04/2019
import functools
import itertools
import operator


def fit1(X, Y, x, y):
    return int(X/x) * int(Y/y)

assert fit1(25, 18, 6, 5) == 12
assert fit1(10, 10, 1, 1) == 100
assert fit1(12, 34, 5, 6) == 10
assert fit1(12345, 678910, 1112, 1314) == 5676
assert fit1(5, 100, 6, 1) == 0


def fit2(X, Y, x, y):
    return max(fit1(X, Y, x, y), fit1(X, Y, y, x))

assert fit2(25, 18, 6, 5) == 15
assert fit2(12, 34, 5, 6) == 12
assert fit2(12345, 678910, 1112, 1314) == 5676
assert fit2(5, 5, 3, 2) == 2
assert fit2(5, 100, 6, 1) == 80
assert fit2(5, 5, 6, 1) == 0


def fit3(X, Y, Z, x, y, z):
    orientations = [
        (x, y, z),
        (x, z, y),
        (y, x, z),
        (y, z, x),
        (z, x, y),
        (z, y, x)
    ]

    return max(int(X/a) * int(Y/b) * int(Z/c) for a, b, c in orientations)

assert fit3(10, 10, 10, 1, 1, 1) == 1000
assert fit3(12, 34, 56, 7, 8, 9) == 32
assert fit3(123, 456, 789, 10, 11, 12) == 32604
assert fit3(1234567, 89101112, 13141516, 171819, 202122, 232425) == 174648


def fitn(crate, box):
    def _fit(c, b):
        return functools.reduce(
            operator.mul,
            (int(x/y) for x, y in zip(c, b)),
            1
        )

    return max(_fit(crate, perm) for perm in itertools.permutations(box))

assert fitn([3, 4], [1, 2]) == 6
assert fitn([123, 456, 789], [10, 11, 12]) == 32604
assert fitn([123, 456, 789, 1011, 1213, 1415], [16, 17, 18, 19, 20, 21]) == 1883443968
