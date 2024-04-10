def C(n, k):
    if n == 0:
        return 1
    elif k == 0 or k == n:
        return 1
    elif k < 0 or k > n:
        return 0
    r = 1
    for i in range(n, n - k, -1):
        r *= i
    for i in range(2, k + 1):
        r //= i
    return r


n, k = map(int, input().split())
s = [0] + list(map(int, input().split()))
r = 0

for i in range(1, k + 1):
    for j in range(s[i - 1], s[i] - 1):
        r += C(n - j - 1, k - i)

print(r)
