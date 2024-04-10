s = input()
n = len(s) // 2

dp = [[0 for _ in range(3 * n + 1)] for _ in range(2 * n + 1)]
dp[0][0] = 1

for i in range(1, 2 * n + 1):
    for j in range(2 * n + 1):
        if j != 2 * n:
            dp[i][j] = dp[i - 1][j + 1]
        dp[i][j] += dp[i - 1][j - 1]

r = 0
d = 0
for i in range(2 * n):
    if s[i] == '(':
        d += 1
    else:
        r += dp[2 * n - i - 1][d + 1]
        d -= 1

print(r)
