# 04/05/2021


def nextpal(n):
    v = [int(i) for i in str(n + 1)]

    for i in range(len(v) // 2):
        if v[-i - 1] > v[i]:
            j = 2
            while (v[-i - j] + 1) // 10:
                v[-i - j] = 0
                j += 1
            v[-i - j] = v[-i - j] + 1

        v[-i - 1] = v[i]

    return int("".join(map(str, v)))


assert nextpal(808) == 818
assert nextpal(999) == 1001
assert nextpal(2133) == 2222
assert nextpal(3 ** 39) == 4052555153515552504

assert nextpal(1) == 2
assert nextpal(998) == 999
assert nextpal(42) == 44
assert nextpal(1337) == 1441
assert nextpal(192) == 202
assert nextpal(1992) == 2002
assert nextpal(199999992) == 200000002
