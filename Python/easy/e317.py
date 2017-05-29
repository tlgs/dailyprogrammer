# 29/05/2017

def collatz(value):
    while value != 'a':
        print(value)
        value = value[2:] + {'a': "bc", 'b': "a", 'c':"aaa"}[value[0]]
    print(value)

#one-liner
collatz1 = lambda y: print("{}".format('\n'.join((lambda a:lambda v:a(a,v))(lambda s, x: [x] + s(s, x[2:] + {'a': "bc", 'b': "a", 'c':"aaa"}[x[0]]) if x != 'a' else [x])(y))))

