n, m = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
p += [0] * (m - n)
q += [0] * (n - m)

s = 0
r = []
for i in range(max(n, m) + 1):
    r.append((p[i] + q[i]) % 998244353)
    if r[i] != 0:
        s = i

print(s)
print(*r[:s+1])

s = 0
r = []
for i in range(n + m + 1):
    r.append(0)
    for j in range(i + 1):
        if j <= n and i - j <= m:
            r[i] = (r[i] + p[j] * q[i - j]) % 998244353
    if r[i] != 0:
        s = i

print(s)
print(*r[:s+1])


s = 0
r = []
for i in range(1000):
    r.append(0 if (i > n) else p[i])
    for j in range(i):
        if i - j <= m:
            r[i] = (r[i] - r[j] * q[i - j]) % 998244353
    if r[i] != 0:
        s = i

print(*r)