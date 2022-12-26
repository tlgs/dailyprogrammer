import string


def base62_encode(n):
    if n == 0:
        return "0"

    r = []
    while n > 0:
        r.append(string.printable[n % 62])
        n //= 62

    return "".join(reversed(r))


assert base62_encode(15674) == "44O"
assert base62_encode(7026425611433322325) == "8n36rbfRcDb"

assert base62_encode(187621) == "MO9"
assert base62_encode(237860461) == "g62n3"
assert base62_encode(2187521) == "9b4B"
assert base62_encode(18752) == "4Ss"

assert base62_encode(0) == "0"
