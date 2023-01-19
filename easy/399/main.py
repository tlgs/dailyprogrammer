def lettersum(s):
    return sum(ord(c) - 96 for c in s)


assert lettersum("") == 0
assert lettersum("a") == 1
assert lettersum("z") == 26
assert lettersum("cab") == 6
assert lettersum("excellent") == 100
assert lettersum("microspectrophotometries") == 317
