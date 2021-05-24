# 24/05/2021


def abacaba(n):
    r = ""
    for i in range(n):
        r = r + chr(97 + i) + r

    return r


assert abacaba(1) == "a"
assert abacaba(2) == "aba"
assert abacaba(3) == "abacaba"
assert abacaba(4) == "abacabadabacaba"
assert abacaba(5) == "abacabadabacabaeabacabadabacaba"

if __name__ == "__main__":
    print(abacaba(26))
