# 21/08/2017

def is_latin_sq(n, l):
    assert len(l) == n**2 
    if len(set(l)) != n:
        return False
    rows = [l[i*n:(i+1)*n] for i in range(n)]
    cols = [l[i:n**2:n] for i in range(n)]
    return all([len(set(r)) == n for r in rows] + [len(set(c)) == n for c in cols])

if __name__ == "__main__":
    n = int(input())
    l = list(map(int, input().split(' ')))
    print(str(is_latin_sq(n, l)))
