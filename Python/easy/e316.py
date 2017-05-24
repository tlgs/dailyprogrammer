# 23/05/2017
# Uses a very un-optimized breadth-first search algorithm

from collections import deque
from math import log, ceil

def knight_move(x, y):
    possible_moves = [(-1, -2), (1, -2), (-1, 2), (1, 2), 
                      (-2, -1), (2, -1), (-2, 1), (2, 1)]

    nodes = deque([(0, 0)])
    counts = 0
    while nodes:
        curr = nodes.popleft()
        if curr == (x, y):
            return ceil(log(counts, 8))
        for node in [tuple(map(sum, zip(curr, move))) for move in possible_moves]:
            nodes.append(node)
        counts += 1
