# 05/04/2017

def bowl_score(sheet):
    total = 0
    score = lambda x: 10 if x[1] == '/' else 20 if x == 'XX' else sum([int(n) for n in x])
    next_ball = lambda x: 10 if x == 'X' else int(x[0])
    next_2_balls = lambda x, y: 10 + next_ball(y[0]) if x == 'X' else score(x[0:2])

    frames = sheet.replace('-', '0').split()
    for i, f in enumerate(frames[:-1]):
        if f[0] == 'X':
            try:
                total += 10 + next_2_balls(frames[i+1], frames[i+2])
            except:
                total += 10 + next_2_balls(frames[i+1], frames[i+1][1])
        elif f[1] == '/':
            total += 10 + next_ball(frames[i+1])
        else:
            total += score(f)

    last = frames[-1]
    total += 10 + next_ball(last[2]) if last[1] == '/' else  \
             10 + next_2_balls(last[1], last[2]) if last[0] == 'X' else \
             score(last)

    return total
