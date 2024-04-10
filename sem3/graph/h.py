def subtract(r, u):
    for i in range(len(u)):
        r[len(r) - len(u) + i] -= u[i]
    return r

def count(z):
    for i in z:
        if z[i]:
            r = dict()
            for v in z:
                r[v] = z[v].copy()
            
            j = r[i].pop()
            r[j].discard(i)

            u = dict()
            for v in z:
                u[v] = z[v].copy()

            for v in u:
                if j in u[v]:
                    u[v].remove(j)
                    u[v].add(i)
            u[i] |= u[j]
            u[i].discard(i)
            u.pop(j)

            return subtract(count(r), count(u))
    return [1] + [0] * (len(z))

n, m = map(int, input().split())

g = {i: set() for i in range(1, n + 1)}

for _ in range(m):
    a, b = map(int, input().split())
    g[a].add(b)
    g[b].add(a)

print(n)
print(*count(g))
