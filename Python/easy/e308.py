# 27/03/2017

grid = ["########=####/#",
        "#     |       #",
        "#     #       #",
        "#     #       #",
        "#######       #",
        "#     _       #",
        "###############"]

grid = [[c for c in grid[y]] for y in range(0, len(grid))]

coords = [(1, 1), (1, 2), (1, 3), (5, 6), (4, 2), (1, 1),
          (1, 2), (5, 5), (5, 5), (9, 1), (7, 5), (2, 2)]

def update_grid(x, y):
    rules = {'S': 'F', ' ': 'S'}
    grid[y][x] = rules[grid[y][x]] if grid[y][x] not in "F#|/=_" else grid[y][x]

    for y in range(0, len(grid)):
        for x in range(0, len(grid[0])):
            if grid[y][x] not in 'F_':
                continue

            try: 
                if grid[y][x] == '_' and not any(['F' in [grid[y][x-1], grid[y][x+1], grid[y-1][x], grid[y+1][x]]]):
                    continue
                else:
                    grid[y][x-1] = 'F' if grid[y][x-1] == 'S' else grid[y][x-1]
                    grid[y][x+1] = 'F' if grid[y][x+1] == 'S' else grid[y][x+1]
                    grid[y-1][x] = 'F' if grid[y-1][x] == 'S' else  grid[y-1][x]
                    grid[y+1][x] = 'F' if grid[y+1][x] == 'S' else  grid[y+1][x]

            except:
                continue

for c in coords:
    update_grid(*c)

print('\n'.join([''.join(l) for l in grid]))