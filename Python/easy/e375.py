# 11/02/2019


def add_one_to_each_digit(n):
    i, total = 0, 0
    while n:
        n, digit = divmod(n, 10)
        total += 10**i * (digit + 1)
        i += (digit == 9) + 1

    return total
