n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

c = [1] + [-i for i in b]

h = 0
s = 0
r = []
for i in range(n):
    r.append(0)
    for j in range(i + 1):
        if j < len(a) and i - j < len(c):
            r[i] += a[j] * c[i - j]
    if r[i] != 0:
        s = i

for i in range(len(c) - 1, -1, -1):
    if c[i] != 0:
        h = i
        break

print(s)
print(*r[:s+1])
print(h)
print(*c[:h+1])