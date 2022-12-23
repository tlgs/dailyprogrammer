#22/02/2017
import random

def game():
    indices = list(range(8))
    places = [None] * 8
    while indices:
        d = random.randint(0,9)
        i = round(d*7/9)
        real_index, c = i, 1
        while not real_index in indices:
            if all(x in indices for x in (i+c, i-c)):
                real_index = i+c if sum(indices)/len(indices) > 3.5 else i-c
            elif i+c in indices:
                real_index = i+c
            elif i-c in indices:
                real_index = i-c
            c += 1
        places[real_index] = str(d)
        indices.remove(real_index)
    return places == sorted(places)

print(sum(game() for _ in range(1000000)) / 10000)
