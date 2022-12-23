# 05/02/2017

def shit_post(word, width, height):
    ln = len(word)-1
    spaced = ' '.join(list(word))
    data = ['']*(ln*height+1)
    for h in range(ln*height+1):
        for w in range(width):
            start = 1 if w>0 else 0
            if h%ln == 0:
                data[h] += spaced[start:] if int(h/ln+w)%2==0 else spaced[::-1][start:]
            else:
                index = h%ln if int(h/ln)%2==0 else ln - h%ln
                middle = word[index] + ' '*(ln*2-1) + word[::-1][index]
                data[h] += middle[start:] if w%2==0 else middle[::-1][start:]
    for l in data:
        print(l)
