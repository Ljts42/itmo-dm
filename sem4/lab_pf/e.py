r = int(input())
d = int(input())
f = list(map(int, input().split()))

c = [[0] * (16) for _ in range(16)]
for i in range(16):
    c[i][0] = 1
    c[i][i] = 1
    for j in range(1, i):
        c[i][j] = c[i - 1][j - 1] + c[i - 1][j]

z = [1, r]
for i in range(18):
    z.append(z[-1] * r)
q = [(-1) ** i * z[i] * c[d + 1][i] for i in range(d + 2)]

a = [0] * 20
for i in range(20):
    s = 1
    for j in f:
        a[i] += j * s
        s *= i
    a[i] *= z[i]

p = []
for i in range(len(q) + len(a)):
    p.append(0)
    for j in range(i + 1):
        if j < len(q) and i - j < len(a):
            p[i] += q[j] * a[i - j]
p = p[:12]

for i in range(len(p) - 1, 0, -1):
    if p[i] == 0:
        p.pop()
    else:
        break

print(len(p) - 1)
print(*p)

for i in range(d + 1, 0, -1):
    if q[i] == 0:
        q.pop()
    else:
        break

print(len(q) - 1)
print(*q)