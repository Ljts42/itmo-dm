def C(x, k):
    r = [1] + [0] * 6
    y = x.copy()
    while k:
        if k % 2 == 1:
            r = P(r, y)
        y = P(y, y)
        k //= 2
    return r

def P(a, b):
    r = [0] * 7
    for i in range(7):
        for j in range(i + 1):
            r[i] += a[j] * b[i - j]
    return r

def L(x):
    r = [1] + [0] * 6
    for i in range(1, 7):
        for j in range(i + 1):
            r[i] += x[j] * r[i - j]
    return r

def S(x):
    r1 = C([1, 1, 1, 1, 1, 1, 1], x[1])
    r2 = C([1, 0, 1, 0, 1, 0, 1], x[2])
    r3 = C([1, 0, 0, 1, 0, 0, 1], x[3])
    r4 = C([1, 0, 0, 0, 1, 0, 0], x[4])
    r5 = C([1, 0, 0, 0, 0, 1, 0], x[5])
    r6 = C([1, 0, 0, 0, 0, 0, 1], x[6])
    return P(r1, P(r2, P(r3, P(r4, P(r5, r6)))))

B = [0, 1, 0, 0, 0, 0, 0]

print(*eval(input()))