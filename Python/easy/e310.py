# 10/04/2017
import random

def kids_lotto(kids, num):
    kids = set(kids.split(';'))
    final = {}
    for k in kids:
        attempt = frozenset(random.sample(kids-{k}, num))
        while attempt in final:
            attempt = frozenset(random.sample(kids-{k}, num))
        final[attempt] = k

    for lotto_list, kid in final.items():
