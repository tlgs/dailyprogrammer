# 15/02/2017

def left_in_bag(input):
    all_tiles =  {'A':9, 'B':2, 'C':2, 'D':4, 'E':12, 'F':2, 'G':3, 'H':2, '_':2,
                  'I':9, 'J':1, 'K':1, 'L':4, 'M':2, 'N':6, 'O':8, 'P':2, 'Q':1,
                  'R':6, 'S':4, 'T':6, 'U':4, 'V':2, 'W':2, 'X':1, 'Y':2, 'Z':1}

    for char in input:
        all_tiles[char] -= 1
        if all_tiles[char] < 0:
            print("Invalid input. More " + char + "'s have been taken from the bag than possible.")
            return

    out = {}
    for letter in all_tiles.keys():
        count = all_tiles[letter]
        if not(count in out.keys()):
            out[count] = [letter]
        else:
            out[count].append(letter)

    for key in out:
        out[key].sort()
        out[key] = ', '.join(out[key])

    for i in range(max(out.keys()), -1, -1):
        if not(i in out.keys()):
            continue
        print('{}: {}'.format(i, out[i]))
