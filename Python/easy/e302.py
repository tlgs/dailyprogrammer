# 06/02/2017
import itertools
import math

periodic = {}
with open('periodic.txt', 'r') as f:
    for lines in f:
        content = lines.split('\t', 2)
        periodic[content[1]] = content[0]

def chem_spell(word):
    pos = 0
    blocks, combinations = [], []
    while pos < len(word):
        for s in periodic.keys():
            if word[pos:pos+len(s)].capitalize() == s:
                blocks.append(s)
        pos += 1
    for i in range(math.ceil(len(word)/2), len(word) + 1):
        combinations.extend(itertools.combinations(blocks, i))
    for x in set(combinations):
        if ''.join(x).lower() == word.lower():
            output = ''.join(x) + ' (' + \
                     ', '.join([periodic[s].lower() for s in x]) + ')'
            print(output)
