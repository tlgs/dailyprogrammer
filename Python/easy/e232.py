# 09/04/2017
from time import time

is_palindrome = lambda x: x == x[::-1]

for dic in ["enable1.txt", "natura.txt"]:
    with open("../../other/" + dic, encoding="utf-8") as f:
        words = {s.strip() for s in f}
    out = []

    start = time()
    for w in words:
        prefix = [w[:i][::-1] for i in range(0, len(w))]
        suffix = [w[i:][::-1] for i in range(0, len(w))]
        for (x, y) in zip(prefix, suffix):
            if x in words and x != w and is_palindrome(w + x):
                out.append(w + " " + x)
            if y in words and y != w and is_palindrome(y + w):
                out.append(y + " " + w)
    elapsed_time = time() - start

    print('{}: Found {} two-word palindromes in {} s.'.format(dic, len(out), elapsed_time))
