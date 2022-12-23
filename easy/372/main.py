# 15/01/2019


def balanced(s):
    return s.count('x') == s.count('y')

assert balanced('xxxyyy') is True
assert balanced('yyyxxx') is True
assert balanced('xxxyyyy') is False
assert balanced('yyxyxxyxxyyyyxxxyxyx') is True
assert balanced('xyxxxxyyyxyxxyxxyy') is False
assert balanced('') is True
assert balanced('x') is False


def balanced_bonus(s):
    return len({s.count(c) for c in s}) <= 1

assert balanced_bonus('xxxyyyzzz') is True
assert balanced_bonus('abccbaabccba') is True
assert balanced_bonus('xxxyyyzzzz') is False
assert balanced_bonus('abcdefghijklmnopqrstuvwxyz') is True
assert balanced_bonus('pqq') is False
assert balanced_bonus('fdedfdeffeddefeeeefddf') is False
assert balanced_bonus('www') is True
assert balanced_bonus('x') is True
assert balanced_bonus('') is True
