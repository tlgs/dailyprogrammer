# 06/03/2017
def permbase2_inv(input):
    return int(input, base=2) + 2**(len(input))-2

def permbase2(input):
    n = 1
    while(2**n <= input):
        input -= 2**n
        n += 1
    return '{0:0{count}b}'.format(input, count = n)
