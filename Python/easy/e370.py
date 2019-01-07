# 07/01/2019


def upc(n):
    digits = [int(x) for x in f'{n:011}']
    M = (sum(digits[0::2]) * 3 + sum(digits[1::2])) % 10
    return 0 if M == 0 else 10 - M

assert upc(4210000526) == 4
assert upc(3600029145) == 2
assert upc(12345678910) == 4
assert upc(1234567) == 0
