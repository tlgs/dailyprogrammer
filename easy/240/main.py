# 11/04/2017
import re
import random

def repl(match):
    w = match.group(0)
    return w[0] + ''.join(random.sample(w[1:-1], len(w)-2)) + w[-1]

print(re.sub(r"\w{3,}", repl, input("Type a sentence to \"typoglicemate\":\n")))
