##
## This piece of code was used to generate a Portuguese wordlist from
## https://raw.githubusercontent.com/titoBouzout/Dictionaries/master/Portuguese%20(European).dic
##
import re

with open("Portuguese (European).txt") as f:
    words = [re.split('[/\s]', s)[0] for s in f.readlines()]

with open("natura.txt", "a+", encoding = "utf-8") as f:
    f.write('\n'.join(words))
