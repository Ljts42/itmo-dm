n, k = map(int, input().split())
 
def ssplit(n, k, p=[[1]], s={1}):
    if len(s) == n:
        if len(p) == k:
            for i in p:
                print(*i)
            print()
        return
    for i in range(p[-1][-1] + 1, n + 1):
        if i not in s:
            ssplit(n, k, p[:-1] + [p[-1] + [i]], s.union({i}))
    if len(p) + 1 == k:
        p += [list(set(range(1, n + 1)).difference(s))]
        ssplit(n, k, p, set(range(1, n + 1)))
        return
    for i in range(2, n + 1):
        if i not in s:
            ssplit(n, k, p + [[i]], s.union({i}))
ssplit(n, k)
