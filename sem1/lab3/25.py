n, k = map(int, input().split())
s = list(map(int, input().split()))
c = k - 1

while c >= 0 and s[c] >= n - (k - c - 1):
    c -= 1
 
if c == -1:
    print(c)
else:
    s[c] += 1

    for i in range(c + 1, k):
        s[i] = s[i - 1] + 1

    print(*s)
