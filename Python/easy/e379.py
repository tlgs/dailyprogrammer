# 18/07/2019


def tax(x):
    brackets = [(0, 10e3), (0.1, 30e3), (0.25, 100e3), (0.4, float('inf'))]
    total = prev = 0
    for rate, cap in brackets:
        step = cap - prev
        prev = cap
        total += int(min(x, step) * rate)
        x = max(0, x - step)

    return total


assert tax(0) == 0
assert tax(10000) == 0
assert tax(10009) == 0
assert tax(10010) == 1
assert tax(12000) == 200
assert tax(56789) == 8697
assert tax(1234567) == 473326
