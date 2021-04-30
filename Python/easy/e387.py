import string
import sys


def caesar(code, shift):
    mapping = {
        c: chr(offset + (ord(c) - offset + shift) % 26)
        for offset, c in zip(
            [65] * 26 + [97] * 26, string.ascii_uppercase + string.ascii_lowercase
        )
    }

    return "".join(mapping.get(c, c) for c in code)


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
