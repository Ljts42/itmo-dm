n = int(input())
g = [[0] * n for _ in range(n)]
for i in range(n):
    s = input()
    for j in range(len(s)):
        g[i][j] = int(s[j])
        g[j][i] = int(s[j])
 
q = list(range(n))
s = 0
for _ in range(n * (n - 1)):
    if not g[q[s]][q[(s+1)%n]]:
        i = 2
        while (not g[q[s]][q[(s+i)%n]]) or (not g[q[(s+1)%n]][q[(s+i+1)%n]]):
            i += 1
        for j in range(i // 2):
            q[(s+1+j)%n], q[(s+i-j)%n] = q[(s+i-j)%n], q[(s+1+j)%n]
    s = (s + 1) % n
 
print(*map(lambda x: x+1, q[s:]), *map(lambda x: x+1, q[:s]))
