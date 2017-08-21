# 21/08/2017

def is_latin_sq(n, l):
    assert len(l) == n**2 and len(set(l)) == n
    rows = [l[i*n:i*n+n] for i in range(n)]
    cols = [[l[i*n + j] for i in range(n)] for j in range(n)]
    return all([len(set(r)) == n for r in rows] + [len(set(c)) == n for c in cols])

if __name__ == "__main__":
    n = int(input())
    l = list(map(int, input().split(' ')))
    print(str(is_latin_sq(n, l)))
