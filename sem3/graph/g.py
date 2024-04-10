from collections import deque

n, m = map(int, input().split())

g = {i: set() for i in range(1, n + 1)}
for _ in range(m):
    a, b = map(int, input().split())
    g[a].add(b)
    g[b].add(a)

u = 1
k = len(g[u])
for i in g:
    k = max(k, len(g[i]))
    if len(g[i]) % 2 == 0:
        u = i

if k % 2 == 0:
    k += 1

t = {u: g[u]}
v = {u} | g[u]
b = deque(g[u])
q = b.copy()
q.appendleft(u)
while b:
    i = b.popleft()
    t[i] = g[i].difference(v)
    v |= t[i]
    b.extend(t[i])
    q.extend(t[i])

c = dict()
v = set()

while q:
    i = q.pop()
    v.add(i)
    z = set(range(1, k + 1))
    for j in g[i].intersection(v):
        z.discard(c[j])
    c[i] = z.pop()

print(k)
for i in range(1, n + 1):
    print(c[i])
