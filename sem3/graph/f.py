from queue import PriorityQueue

n = int(input())
p = list(map(int, input().split()))
d = dict()
for i in p:
    d.setdefault(i, 0)
    d[i] += 1

g = PriorityQueue()

s = set(p)
for i in range(1, n + 1):
    if not i in s:
        g.put(i)

p.reverse()
while p:
    u = p.pop()
    v = g.get()
    d[u] -= 1
    if d[u] == 0:
        g.put(u)
    print(u, v)
print(g.get(), g.get())
