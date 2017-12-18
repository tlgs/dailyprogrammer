# 18/12/2017

def baum_sweet(n):
    seq = []
    for i in range(1, n+1):
        count, flag = 0, False
        for c in bin(i)[2:]+'1':
            if int(c) and count > 0 and count % 2 == 1:
                flag = True
                break
            count = 0 if int(c) else count + 1
        seq.append("0" if flag else "1")
    print(", ".join(seq))
