# 15/03/2018


def leaps(start, end):
    def is_leap(y):
        return (y % 4 == 0 and not y % 100 == 0) or (y % 900 in [200, 600])

    t, r = divmod(end - start, 900)
    return t*218 + sum(is_leap(y) for y in range(start, start+r))

assert leaps(2016, 2017) == 1
assert leaps(2019, 2020) == 0
assert leaps(1900, 1901) == 0
assert leaps(2000, 2001) == 1
assert leaps(2800, 2801) == 0
assert leaps(123456, 123456) == 0
assert leaps(1234, 5678) == 1077
assert leaps(123456, 7891011) == 1881475
