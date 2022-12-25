import sys
import random


def rolls(raw):
    n, m = map(int, raw.split("d", maxsplit=1))
    return tuple(random.randint(1, m) for _ in range(n))


def main():
    print("Interactive dice roller ('NdM' format)\n")
    while True:
        try:
            raw_die = input(">> ")
        except KeyboardInterrupt:
            break

        t = rolls(raw_die)
        print(sum(t), ": ", " ".join(str(x) for x in t), sep="", end="\n\n")


if __name__ == "__main__":
    raise SystemExit(main())
