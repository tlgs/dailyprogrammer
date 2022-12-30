def bitstring(n):
    return n.bit_count()


assert bitstring(23) == 4

assert bitstring(0) == 0
assert bitstring(1) == 1
assert bitstring(2) == 1
assert bitstring(3) == 2
