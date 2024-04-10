n = int(input())

def tsplit(n, p=[]):
    if n == 0:
        print(*p, sep='+')
        return

    q = 1
    if len(p) > 0:
        q = p[-1]

    for i in range(q, n + 1):
        tsplit(n - i, p + [i])

tsplit(n)
