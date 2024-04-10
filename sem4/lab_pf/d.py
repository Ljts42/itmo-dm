from fractions import Fraction as f

r, m = map(int, input().split())
pk = list(map(int, input().split()))

def p(a, b):
    r = [f(0) for _ in range(m + 1)]
    for i in range(m + 1):
        for j in range(i + 1):
            if j < len(a) and i - j < len(b):
                r[i] += a[j] * b[i - j]
    return r

def s(a, b):
    r = [f(0) for i in range(m + 1)]
    for i in range(m + 1):
        if i < len(a):
            r[i] += a[i]
        if i < len(b):
            r[i] += b[i]
    return r

def h(a, b):
    return [f(i) * b for i in a]

def d(a, b):
    # r = [f(a[i]) if i < len(a) else f(0) for i in range(m + 1)]
    # for i in range(m + 1):
    #     for j in range(i):
    #         if i - j < len(b):
    #             r[i] -= r[j] * b[i - j]
    # return r
    return [f(i) / b for i in a]

def c(j, k):
    r = [f(-j), f(1)]
    for i in range(2, k + 1):
        r = d(p(r, [k - j, 1]), i)
    return r

fk = [f(0) for _ in range(m + 1)]
for i in range(m):
    fk = s(fk, d(h(c(i, m), pk[i]), r ** i))

print(*fk)