# 15/03/2017

def gray_code_seq(n):
    if n == 1:
        return ['0', '1']
    else:
        return ['0' + i for i in gray_code_seq(n-1)] + \
               ['1' + i for i in gray_code_seq(n-1)[::-1]]
