# 16/02/2018
import sys

def ffd(s, b):
    """First Fit Decreasing algorithm
    1.Sort the items to be inserted in decreasing order by size
    2.Go through the items in sorted order
        1.Try to place the item in the first bin that will accommodate it
        2.If no bin is found, start a new bin
    """
    #shelf -> [id, capacity, available, book list]
    #book  -> (title, width)
    s = sorted(s, key=lambda x: x[1], reverse=True)
    b = sorted(b, key=lambda x: x[1], reverse=True)
    for book in b:
        for shelf in s:
            if shelf[2] > book[1]:
                shelf[3].append(book[0])
                shelf[2] -= book[1]
                break
            elif shelf[1] == shelf[2] and not shelf[2] > book[1]:
                return None

    return list(filter(lambda x: len(x[3]) > 0, s))

if __name__ == "__main__":
    shelves = [[n, int(capacity), int(capacity), []] for n, capacity in enumerate(sys.stdin.readline().split())]
    books = []
    for line in sys.stdin.readlines():
        w, t = line.split(maxsplit=1)
        books.append((t.strip(), int(w)))

    solution = ffd(shelves, books)
    if solution is None:
        print("Impossible")
    else:
        print(len(solution), " shelves used")
        print('\n'.join("{}: {}".format(s[0], s[3]) for s in solution))
