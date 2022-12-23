# 04/09/2017

def bound_rect(circles):
    up = max([c[1] + c[2] for c in circles])
    down = min([c[1] - c[2] for c in circles])
    right = max([c[0] + c[2] for c in circles])
    left = min([c[0] - c[2] for c in circles])
    vertices = [(left, down), (left, up), (right, up), (right, down)]
    return ', '.join("({:.3f}, {:.3f})".format(*v) for v in vertices)
