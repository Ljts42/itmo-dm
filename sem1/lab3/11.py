n = int(input())

def subset(n, p=[]):
    q = 0

    if len(p) > 0:
        q = p[-1]

    for i in range(q, n + 1):
        if i == q:
            print(*p)
        else:
            subset(n, p + [i])

subset(n)
