# 24/03/2017

def garland(string):
    for i in range(1, len(string)):
        if string[:-i] == string[i:]:
            return len(string) - i
    return 0


for dic in ["enable1.txt", "natura.txt"]:
    with open(dic, encoding="utf-8") as f:
        words = [s.strip() for s in f.readlines()]

    print("searching {}...".format(dic))
    best = max(words, key=garland)
    print("{} ({})".format(best, garland(best)))
