import decimal
from decimal import Decimal
decimal.getcontext().prec=200

n = int(input())
d = list(map(int, input().split()))
s = input()
m = sum(d)
for i in range(1, n):
    d[i] += d[i - 1]
d = [0] + d
s = Decimal(int(s, 2)) / Decimal(2 ** len(s))
l = Decimal(0)
r = Decimal(1)
for _ in range(m):
    for i in range(1, n + 1):
        nl = l + Decimal(r - l) * Decimal(d[i - 1]) / Decimal(m)
        nr = l + Decimal(r - l) * Decimal(d[i]) / Decimal(m)
        if nl <= s < nr:
            print(chr(96 + i), end='')
            l, r = nl, nr
            break
print()
