# 05/05/2018

def paperfold(n):
    seq = ["1"]
    for _ in range(n):
        for i, x in zip(range(0, len(seq)*2+1, 2), [x%2 for x in range(1, len(seq)+2)]):
            seq.insert(i, str(x))

    return ' '.join(seq)