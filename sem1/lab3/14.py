n = int(input())
s = list(map(int, input().split()))
fs = [0] * (n - 1)

for i in range(n - 1):
    for j in range(i + 1, n):
        if s[i] > s[j]:
            fs[i] += 1
 
r = 0
for k in range(1, n):
    r += fs[k - 1]
    r *= n - k
 
print(r)
