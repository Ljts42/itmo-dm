import sys

sys.stdin = open('check.in', 'r')
sys.stdout = open('check.out', 'w')

n, m = map(int, input().split())
I = set()
for _ in range(m):
    a = list(map(int, input().split()))[1:]
    s = 0
    for i in a:
        s += 1 << (i - 1)
    I.add(s)

r = 0 in I
for A in I:
    if not r:
        break
    for B in range(1, A):
        if (A ^ B == A - B) and not (B in I):
            r = False
            break
for A in I:
    if not r:
        break
    for B in I:
        if bin(A).count('1') > bin(B).count('1'):  # |A| > |B|
            r = False
            d = A ^ A & B  # |A \ B|
            for k in range(n):
                if (1 << k) & d:  # k ∈ |A \ B|
                    if (B | (1 << k)) in I:  # B ∪ {k} ∈ I
                        r = True
                        break
            if not r:
                break

print('YES' if r else 'NO')