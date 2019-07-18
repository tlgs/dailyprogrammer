# 18/07/2019


def tax(x):
    cap = [10e3, 30e3, 100e3]
    steps = [a - b for a, b in zip(cap, [0] + cap[:-1])]
    rate = [0, 0.1, 0.25, 0.4]
    t = 0

    for s, r in zip(steps, rate[:-1]):
        x -= s
        if x < 0:
            t += (s + x) * r
            return int(t)
        else:
            t += s * r

    return int(t + x * rate[-1])

assert tax(0) == 0
assert tax(10000) == 0
assert tax(10009) == 0
assert tax(10010) == 1
assert tax(12000) == 200
assert tax(56789) == 8697
assert tax(1234567) == 473326
