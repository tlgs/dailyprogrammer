def guess(low, high):
    v = (high + low) // 2
    print(f"Is your number {v}? (y)es, (l)ower, or (h)igher")
    match input():
        case "y":
            return
        case "l":
            guess(low, v - 1)
        case "h":
            guess(v + 1, high)
        case x:
            raise ValueError(x)


if __name__ == "__main__":
    guess(1, 100)
