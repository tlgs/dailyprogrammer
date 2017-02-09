# 09/02/2017

def polite_seq(n):
    odd = lambda x: [odd for odd in range(3, x+1, 2) if x%odd==0]
    divisors = odd(n)
    sequences = [[] for i in range(len(divisors))]
    for i in range(len(divisors)):
        d = divisors[i]
        for j in range(int(abs(n/d - d/2)) + 1, int(n/d + d/2 + 1)):
            sequences[i].append(j)
    for x in sequences:
        print(''.join(str(x)))
