# 28/04/2021
import sys


def caesar(code, shift):
    mapping = {
        n: start + (n - start + shift) % 26
        for start, n in zip(
            [65] * 26 + [97] * 26, list(range(65, 91)) + list(range(97, 123))
        )
    }

    return code.translate(mapping)


if __name__ == "__main__":
    with open("/usr/share/dict/words") as f:
        word_list = set(x.strip() for x in f.readlines())

    code = sys.stdin.read()
    counts = []
    for shift in range(26):
        x = sum(word in word_list for word in caesar(code, shift).split())
        counts.append(x)

    guess, _ = max(enumerate(counts), key=lambda t: t[1])
    print(f"{guess}: {caesar(code, guess)}")
