from queue import PriorityQueue

n = int(input())
g = dict()
for _ in range(n - 1):
    i, j = map(int, input().split())
    g.setdefault(i, set())
    g.setdefault(j, set())
    g[i].add(j)
    g[j].add(i)

z = PriorityQueue()
for v in g:
    if len(g[v]) == 1:
        z.put(v)

r = []
while len(r) < n - 2:
    v = z.get()
    c = g[v].pop()
    r.append(c)

    g[c].remove(v)
    if len(g[c]) == 1:
        z.put(c)

print(*r)
