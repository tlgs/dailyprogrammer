# 23/05/2017
from queue import Queue

class Node(object):
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent

def knight_move(x, y):
    possible_moves = [(-1, -2), (1, -2), (-1, 2), (1, 2), 
                      (-2, -1), (2, -1), (-2, 1), (2, 1)]

    nodes = Queue()
    nodes.put(Node(tuple([0, 0]), None))
    visited = {(0,0)}

    while nodes:
        curr = nodes.get()
        if curr.value == (x, y):
            break
        for node in [tuple(map(sum, zip(curr.value, move))) for move in possible_moves]:
            if node not in visited:
                visited |= set(node)
                nodes.put(Node(node, parent=curr))
                
    path = []
    while curr is not None:
        path.append(str(curr.value))
        curr = curr.parent
    print('{}'.format(" -> ".join(path[::-1])))

    return len(path) - 1
