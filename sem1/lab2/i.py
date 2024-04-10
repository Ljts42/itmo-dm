from random import randint as rnd

if input() == '1':
    s = [rnd(0, 1) for _ in range(rnd(1, 100000))]
    print(''.join(map(str, s)))
    # s = list(map(int, list(input())))

    n, k, p = len(s), 0, 1
    while p < n + k + 1:
        k += 1
        p *= 2

    r = [0] * (n + k)
    c = 0
    for i in range(n + k):
        if bin(i + 1).count('0') + 2 != len(bin(i + 1)):
            r[i] = s[c]
            for j in range(k):
                if bin(i + 1)[2:].rjust(k, '0')[j] == '1':
                    r[2 ** (k - j - 1) - 1] ^= s[c]
            c += 1

    print(*r, sep='')
else:
    s = list(map(int, list(input())))

    n, k, p = len(s), 0, 1
    while p < n - k + 1:
        k += 1
        p *= 2
    n -= k

    r = [0] * n
    c = 0
    z = [0] * k
    for i in range(n + k):
        for j in range(k):
            if bin(i + 1)[2:].rjust(k, '0')[j] == '1':
                z[j] ^= s[i]

    z = int(''.join(map(str, z)), 2)
    if z > 0 and bin(z).count('0') + 2 != len(bin(z)):
        s[z - 1] = 1 - s[z - 1]

    c = 0
    for i in range(n + k):
        if bin(i + 1).count('0') + 2 != len(bin(i + 1)):
            r[c] = s[i]
            c += 1

    print(*r, sep='')
