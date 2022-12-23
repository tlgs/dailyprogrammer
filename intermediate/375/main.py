# 15/02/2019
# influenced heavily by Gprime5's solution


def flip(cards):
    order = []
    direction = True
    for i, card in enumerate(cards):
        if direction:
            order.insert(0, str(i))
        else:
            order.append(str(i))
        direction ^= (card == '1')

    return ' '.join(order) if not direction else 'no solution'
