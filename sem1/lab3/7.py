n = int(input())
 
def perm(n, p=[]):
    if len(p) == n:
        print(*p)
        return
    for i in range(1, n + 1):
        if i not in p:
            perm(n, p + [i])
 
perm(n)
