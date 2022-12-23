# 23/03/2017

def get_children(string, p):
    if string not in words_dict.keys():
        return False

    if len(string) == 2:
        p.append(string)
        return True

    if get_children(string[1:], p):
        p.append(string)
        return True
    elif get_children(string[:-1], p):
        p.append(string)
        return True

with open("enable1.txt") as f:
    words = sorted(list(map(str.strip, f.readlines())), key=len, reverse=True)
    words_dict = dict(zip(words, [None]*len(words)))
    i, path = 0, []
    size = 0
    while True:
        if size > len(words[i]):
            break
        elif get_children(words[i], path):
            size = len(words[i])
            print(' -> '.join(path))
            path = []
        i += 1
