from string import ascii_lowercase


def caesar(plaintext, *, shift):
    n = shift % 26
    mapping = str.maketrans(ascii_lowercase, ascii_lowercase[n:] + ascii_lowercase[:n])
    return plaintext.translate(mapping)


assert caesar("veni, vidi, vici", shift=3) == "yhql, ylgl, ylfl"
assert caesar("veni, vidi, vici", shift=13) == "irav, ivqv, ivpv"
