# 23/04/2017

def longest_word(letters):
    with open("../../other/enable1.txt", "r") as f:
        ans = max([w.strip() for w in f.readlines() if set(w.strip()).issubset(letters)], key=len)
    print("{} -> {}".format(letters, ans))
