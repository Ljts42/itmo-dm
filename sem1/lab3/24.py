n = int(input())
s = list(map(int, input().split()))

r = [0] * n
if s == list(range(1, n + 1)):
    print(*r)
else:
    for i in range(n - 1, 0, -1):
        if s[i] < s[i - 1]:
            m = i + 1
            for j in range(i + 1, n - 1)