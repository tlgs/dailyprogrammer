# 05/02/2017

def not_McNugget(n):
    mcn = lambda x: x != 3 and (x > 43 or x % 3 == 0)
    for i in range(1, n+1):
        d = i
        while i >= 0:
            if mcn(i): break
            i -= 20
        else: print(d)
