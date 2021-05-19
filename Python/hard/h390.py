# 18/05/2021

import math


def f(n):
    total = 0
    for i in range(0, int(math.log10(n)) + 1):
        e = 10 ** i

        digit = (n // e) % 10
        prefix = n // (e * 10)

        if digit == 0:
            total += prefix * e
        elif digit == 1:
            total += prefix * e + (n % e) + 1
        else:
            total += (prefix + 1) * e

    return total


assert f(1) == 1
assert f(5) == 1
assert f(10) == 2
assert f(20) == 12
assert f(1234) == 689
assert f(5123) == 2557
assert f(70000) == 38000
assert f(123321) == 93395
assert f(3 ** 35) == 90051450678399649

assert int(math.log10(f(5 ** 20)) + 1) == 15
assert sum(int(x) for x in str(f(5 ** 20))) == 74


if __name__ == "__main__":
    total = 0
    n = 1
    while n < 10 ** 11:
        y = f(n)
        if n == y:
            total += n
            n += 1
        else:
            n += max(abs(n - y) // int(math.log10(n) + 1), 1)

    assert int(math.log10(total) + 1) == 11
    assert sum(int(x) for x in str(total)) == 53
