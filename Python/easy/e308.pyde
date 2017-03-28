# 27/03/2017
# Using Processing.py

grid = ["########=####/#",
        "#     |       #",
        "#     #       #",
        "#     #       #",
        "#######       #",
        "#     _       #",
        "###############"]

grid = [[c for c in grid[y]] for y in range(0, len(grid))]

map_color = {'S': (170, 170, 170), 'F': (255, 140, 0), '#': (0, 0, 0),
             '|': (119, 92, 51), '/': (188, 145, 81), '=': (70, 0, 0), 
             '_': (248, 135, 255), ' ': (255, 255, 255)}
        
coords = [(1, 1), (1, 2), (1, 3), (5, 6), (2, 2), (1, 1), 
          (1, 2), (5, 5), (5, 5), (9, 1), (7, 5)]

offset = 20

def update_grid(x, y):
    rules = {'S': 'F', ' ': 'S'}
    grid[y][x] = rules[grid[y][x]] if grid[y][x] not in "F#|/=_" else grid[y][x]

    for y in range(0, len(grid)):
        for x in range(0, len(grid[0])):
            if grid[y][x] not in 'F_':
                continue
            else: 
                if grid[y][x] == '_' and not any(['F' in [grid[y][x-1], grid[y][x+1], grid[y-1][x], grid[y+1][x]]]):
                    continue
                else:
                    grid[y][x-1] = 'F' if grid[y][x-1] == 'S' and x > 0 else grid[y][x-1]
                    grid[y][x+1] = 'F' if grid[y][x+1] == 'S' and x < len(grid[0]) else grid[y][x+1]
                    grid[y-1][x] = 'F' if grid[y-1][x] == 'S' and y > 0 else  grid[y-1][x]
                    grid[y+1][x] = 'F' if grid[y+1][x] == 'S' and y < len(grid) else  grid[y+1][x]

def update_colors():
    colors = [[map_color[grid[y][x]] for x in range(0, len(grid[0]))] for y in range(0, len(grid))]

    for y in range(0, len(grid)):
        for x in range(0, len(grid[0])):
            noStroke()
            fill(*colors[y][x])
            rect(x*20 + offset, y*20 + offset, 20, 20)

def setup():
    size(15*20 + 2*offset, 7*20 + 2*offset)
    update_colors()
    
count = 0
    
def draw():
    global count
    if count >= len(coords) - 1:
        noLoop()
    delay(1000)
    update_grid(*coords[count])
    update_colors()
    count += 1
