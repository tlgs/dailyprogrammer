# 23/05/2017
# BFS implementation with Manhattan distance heuristic
from queue import Queue

class Node(object):
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent

def knight_move(x, y):
    possible_moves = [(-1, -2), (1, -2), (-1, 2), (1, 2), 
                      (-2, -1), (2, -1), (-2, 1), (2, 1)]

    manhattan = lambda tile: abs(x - tile[0]) + abs(y - tile[1])
    best_distance = manhattan((0,0))

    nodes = Queue()
    nodes.put(Node((0, 0), None))
    visited = {(0,0)}

    found = False
    while nodes:
        curr = nodes.get()

        for (dx, dy) in possible_moves:
            tile = (curr.value[0] + dx, curr.value[1] + dy)
            if tile == (x,y):
                curr = Node(tile, curr)
                found = True
                break

            if manhattan(tile) > best_distance + 3:
                continue
            elif manhattan(tile) < best_distance:
                best_distance = manhattan(tile)
            
            if tile not in visited:
                visited |= set(tile)
                nodes.put(Node(tile, parent=curr))

        if found:
            break

    path = []
    while curr is not None:
        path.append(str(curr.value))
        curr = curr.parent
    print('{}'.format(" -> ".join(path[::-1])))

    return len(path) - 1
