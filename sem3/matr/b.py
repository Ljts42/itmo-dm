import sys, queue


sys.stdin = open('destroy.in', 'r')
sys.stdout = open('destroy.out', 'w')

n, m, s = map(int, input().split())
g = [[] for _ in range(n + 1)]
d = dict()
for i in range(1, m + 1):
    a, b, c = map(int, input().split())
    g[a].append([-c, b, i])
    g[b].append([-c, a, i])
    d[i] = c
v = set()
v.add(1)
q = queue.PriorityQueue()
for i in g[1]:
    q.put(i)
t = [0, 0, 0]
while len(v) < n:
    while not q.empty():
        t = q.get()
        if not (t[1] in v):
            break
    v.add(t[1])
    for i in g[t[1]]:
        q.put(i)
    d.pop(t[2])
r = []
for e in sorted(d.items(), key=lambda x: x[1]):
    if s < e[1]:
        break
    s -= e[1]
    r.append(e[0])
r.sort()
print(len(r))
print(*r)
