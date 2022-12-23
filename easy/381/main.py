# 12/11/2019


def yahtzee_upper(r):
    return max(i * r.count(i) for i in set(r))


assert yahtzee_upper([2, 3, 5, 5, 6]) == 10
assert yahtzee_upper([1, 1, 1, 1, 3]) == 4
assert yahtzee_upper([1, 1, 1, 3, 3]) == 6
assert yahtzee_upper([1, 2, 3, 4, 5]) == 5
assert yahtzee_upper([6, 6, 6, 6, 6]) == 30


def yahtzee_upper_bonus(r):
    n = {}
    for i in r:
        n[i] = n.get(i, 0) + i

    return max(n.values())


if __name__ == "__main__":
    import sys
    import time

    rolls = [int(x) for x in sys.stdin.readlines()]
    s = time.time()
    yahtzee_upper_bonus(rolls)
    print(f"{time.time() - s:.5f} seconds")
