inp = input().strip()
ind = 0

def next():
    global ind, inp
    ind += 1
    return inp[ind - 1]

def binom(n, k):
    if n < k:
        return 0
    if k == 0 or k == n:
        return 1
    if k == 1 or k == n - 1:
        return n
    return binom(n - 1, k - 1) * n // k

cache = {}
def binom_cached(n, k):
    if (n, k) in cache:
        return cache[(n, k)]
    res = binom(n, k)
    cache[(n, k)] = res
    return res

def parse():
    c = next()
    if c == 'B':
        return [0, 1, 0, 0, 0, 0, 0]
    elif c == 'L':
        next() # '('
        arg = parse()
        next() # ')'
        res = [1] + [0]*6
        for i in range(1, len(res)):
            for j in range(1, i+1):
                res[i] += arg[j] * res[i - j]
        return res
    elif c == 'S':
        next() # '('
        arg = parse()
        next() # ')'
        dp = [[0]*7 for _ in range(7)]
        for i in range(7):
            dp[i][0] = 1
        for i in range(1, 7):
            for j in range(1, i+1):
                for k in range(i // j + 1):
                    dp[i][j] += binom_cached(arg[j] + k - 1, k) * dp[i - j * k][j - 1]
        res = [dp[i][i] for i in range(7)]
        print(dp)
        return res
    elif c == 'P':
        next() # '('
        left = parse()
        next() # ','
        right = parse()
        next() # ')'
        res = [0]*7
        for i in range(len(res)):
            for j in range(i+1):
                res[i] += left[j] * right[i - j]
        return res

res = parse()
print(*res)