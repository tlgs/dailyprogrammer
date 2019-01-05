# 05/01/2018


def hexcolor(red, green, blue):
    return f'#{red:02X}{green:02X}{blue:02X}'

assert hexcolor(255, 99, 71) == '#FF6347'
assert hexcolor(184, 134, 11) == '#B8860B'
assert hexcolor(189, 183, 107) == '#BDB76B'
assert hexcolor(0, 0, 205) == '#0000CD'


def blend(colors):
    total = (0, 0, 0)
    for color in colors:
        rgb = (color[1:3], color[3:5], color[5:])
        rgb = tuple(int(x, 16) for x in rgb)
        total = tuple(x + y for x, y in zip(total, rgb))

    red, green, blue = tuple(round(x / len(colors)) for x in total)

    return f'#{red:02X}{green:02X}{blue:02X}'

assert blend(['#000000', '#778899']) == '#3C444C'
assert blend(['#E6E6FA', '#FF69B4', '#B0C4DE']) == '#DCB1D9'
