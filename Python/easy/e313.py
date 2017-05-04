# 01/05/2017

def subset_sum(l):
    for x in range(1, 2**len(l)):
        numbers_to_add = [l[i] for i in range(0, len(l)) if x & (1 << i)]
        if sum(numbers_to_add) is 0:
            return True
    return False
