# 12/03/2017
from string import ascii_lowercase, ascii_uppercase

def make_table(mirrors):
    table = [[]]*15
    table[0] = ' ' + ascii_lowercase[0:13] + ' '
    table[14] = ' ' + ascii_uppercase[13:] + ' '
    for i in range(1, 14):
        table[i] = ascii_uppercase[i-1] + mirrors[i-1] + ascii_lowercase[12+i]
    return table

def get_letter(c, table):
    #get starting position / velocities
    if c in ascii_uppercase[0:13] or c in ascii_lowercase[13:]:
        x = 1 if c in ascii_uppercase else 13
        y = 1 + (ascii_uppercase.index(c) if c in ascii_uppercase else ascii_lowercase[13:].index(c))
        dx = 1 if c in ascii_uppercase else -1
        dy = 0
    else:
        x = 1 + (ascii_uppercase[13:].index(c) if c in ascii_uppercase else ascii_lowercase.index(c))
        y = 1 if c in ascii_lowercase else 13
        dx = 0
        dy = 1 if c in ascii_lowercase else -1

    #go through the grid
    while(x in range(1, 14) and y in range(1, 14)):
        if table[y][x] == '/':
            tmp = 1 if dy == -1 else -1 if dy == 1 else 0
            dy = 1 if dx == -1 else -1 if dx == 1 else 0
            dx = tmp
        elif table[y][x] == '\\':
            tmp = 1 if dy == 1 else -1 if dy == -1 else 0
            dy = 1 if dx == 1 else -1 if dx == -1 else 0
            dx = tmp
        x += dx
        y += dy

    return table[y][x]

def decode(key, target):
    tb = make_table(key)
    return ''.join([get_letter(c, tb) for c in target])

empty_mirrors = [' '*13]*13
challenge_mirrors = ['   \\\\  /\    ',
                     '            \\',
                     '   /         ',
                     '      \\     \\',
                     '    \\        ',
                     '  /      /   ',
                     '\\  /      \\  ',
                     '     \       ',
                     '\\/           ',
                     '/            ',
                     '          \\  ',
                     '    \\/       ',
                     '   /       / ']
