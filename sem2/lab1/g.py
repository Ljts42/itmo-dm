import sys

sys.stdin = open('equivalence.in')
sys.stdout = open('equivalence.out', 'w')

g = set()
n1, m1, k1 = map(int, input().split())
f1 = set(map(int, input().split()))

t1 = [dict() for _ in range(n1 + 1)]
for _ in range(m1):
    a, b, c = input().split(' ', 2)
    a, b, c = int(a), int(b), c[0]
    t1[a][c] = b
    g.add(c)

n2, m2, k2 = map(int, input().split())
f2 = set(map(int, input().split()))

t2 = [dict() for _ in range(n2 + 1)]
for _ in range(m2):
    a, b, c = input().split(' ', 2)
    a, b, c = int(a), int(b), c[0]
    t2[a][c] = b
    g.add(c)

def check():
    visited = [[False] * (n2 + 1) for _ in range(n1 + 1)]
    q = [[1, 1]]
    while len(q) != 0:
        s1, s2 = q.pop()
        if (s1 in f1) != (s2 in f2):
            return False
        visited[s1][s2] = True
        for c in g:
            if not visited[t1[s1].get(c, 0)][t2[s2].get(c, 0)]:
                q.append([t1[s1].get(c, 0), t2[s2].get(c, 0)])
    return True

if check():
    print('YES')
else:
    print('NO')
