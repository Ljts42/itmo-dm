n = int(input())
g = dict()
for i in range(n):
    s = input()
    for j in range(len(s)):
        g.setdefault(i + 1, set())
        g.setdefault(j + 1, set())
        if s[j] == '1':
            g[i + 1].add(j + 1)
        else:
            g[j + 1].add(i + 1)

p = [1]
for v in range(2, n + 1):
    i = 0
    while i < len(p) and v in g[p[i]]:
        i += 1
    p = p[:i] + [v] + p[i:]

k = n - 1
while k > 0 and not (p[0] in g[p[k]]):
    k -= 1

r = p[:k+1]
while len(r) < n:
    v = p.pop()
    i = 0
    while i < len(r) and not (r[i] in g[v]):
        i += 1
    r = r[:i] + [v] + r[i:]

print(*r)
