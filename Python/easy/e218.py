# 17/10/2018
import sys


def palindromic(x, i):
    if str(x) == str(x)[::-1]:
        return (x, i)
    else:
        return palindromic(x + int(str(x)[::-1]), i + 1)

if __name__ == "__main__":
    result = palindromic(int(sys.argv[1]), 0)
    print("{} gets palindromic after {} steps: {}".format(sys.argv[1],
                                                          result[1],
                                                          result[0]))
