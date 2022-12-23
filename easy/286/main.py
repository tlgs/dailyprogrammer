# 31/01/2017

def reverse_factorial(n, f=2):
    if n == 1:
        return str(f-1) + "!"
    elif n%f != 0:
        return "NONE"
    return reverse_factorial(n/f, f+1)
