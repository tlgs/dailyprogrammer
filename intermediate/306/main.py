# 15/03/2017

def gray_code_seq(n):
    if n == 1:
        return ['0', '1']
    else:
        return ['0' + i for i in gray_code_seq(n-1)] + \
               ['1' + i for i in gray_code_seq(n-1)[::-1]]

def gray_code_seq2(n):
    seq = []
    for i in range(0, 2**n):
        g = i ^ (i >> 1)
        seq.append("{:0{l}b}".format(g, l=n))
    return seq
