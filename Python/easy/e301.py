# 02/01/2017
import re
from collections import OrderedDict

def create_regex(pattern):
    oset_pattern = list(OrderedDict.fromkeys(pattern))
    regex_pattern = ['([a-z])' if (not char in pattern[:i])
                    else "\\" + str(oset_pattern.index(char)+1)
                    for i, char in enumerate(pattern)]
    return ''.join(['[\\S]*'] + regex_pattern + ['[\\S]*'])

def test_pattern(pattern):
    regex_pattern = create_regex(pattern)
    with open('enable1.txt', 'r') as f:
        print("".join([line for line in f if re.match(regex_pattern, line, re.I)]))
