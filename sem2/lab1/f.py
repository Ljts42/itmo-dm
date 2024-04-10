import sys

sys.stdin = open('isomorphism.in')
sys.stdout = open('isomorphism.out', 'w')

g = set()
n1, m1, k1 = map(int, input().split())
f1 = set(map(int, input().split()))

t1 = [dict() for _ in range(n1 + 1)]
d1 = [True] * (n1 + 1)
for _ in range(m1):
    a, b, c = input().split(' ', 2)
    a, b, c = int(a), int(b), c[0]
    t1[a][c] = b
    if a != b:
        d1[a] = False
    g.add(c)

n2, m2, k2 = map(int, input().split())
f2 = set(map(int, input().split()))

t2 = [dict() for _ in range(n2 + 1)]
d2 = [True] * (n2 + 1)
for _ in range(m2):
    a, b, c = input().split(' ', 2)
    a, b, c = int(a), int(b), c[0]
    t2[a][c] = b
    if a != b:
        d2[a] = False
    g.add(c)

visited = [False] * max(n1 + 1, n2 + 1)
assoc = dict()

def dfs(u1, u2):
    global visited, assoc

    visited[u1] = True
    if (u1 in f1) != (u2 in f2):
        return False

    assoc[u1] = u2
    result = True
    for char in g:
        h1 = t1[u1].get(char, 0)
        h2 = t2[u2].get(char, 0)
        if (d1[h1]) != (d2[h2]):
            return False
        elif visited[h1]:
            result &= (h2 == assoc[h1])
        else:
            result &= dfs(h1, h2)
    return result

if dfs(1, 1):
    print('YES')
else:
    print('NO')
