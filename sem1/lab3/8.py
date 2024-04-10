n, k = map(int, input().split())
 
def comb(n, k, p=[]):
    if len(p) == k:
        print(*p)
        return
    q = 0
    if len(p) > 0:
        q = p[-1]
    for i in range(q + 1, n + 1):
        comb(n, k, p + [i])
 
comb(n, k)
