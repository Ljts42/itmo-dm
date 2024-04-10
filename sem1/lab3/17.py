n, k = map(int, input().split())
k += 1

dp = [[0 for _ in range(n + 2)] for _ in range(2 * n + 1)]
dp[0][0] = 1

for i in range(1, 2 * n + 1):
    for j in range(n + 1):
        if j != 2 * n:
            dp[i][j] += dp[i - 1][j + 1]
        dp[i][j] += dp[i - 1][j - 1]

r = ''
d = 0
for i in range(2 * n):
    if dp[2 * n - i - 1][d + 1] >= k:
        d += 1
        r += '('
    else:
        k -= dp[2 * n - i - 1][d + 1]
        d -= 1
        r += ')'
print(r)
