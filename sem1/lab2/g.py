import decimal
from decimal import Decimal
decimal.getcontext().prec=1000

from random import randint, choice
from string import ascii_letters
# text = [random.choice(string.ascii_lowercase + string.digits if i != 5 else string.ascii_uppercase) for i in range(10)]
# file = open('g.txt', 'w')
lett = ascii_letters[:26]
for _ in range(1):
    n = int(input())
    # s = ''.join([choice(lett) for i in range(randint(1, 100))])
    # n = min(26, ord(max(s)) - 96)
    print(n)
    # file.write(str(n) + '\n')
    s = input()
    print(s)
    print()
    print(n)
    # file.write(s + '\n\n' + str(n) + '\n')
    d = [0] * n
    for i in range(len(s)):
        d[ord(s[i]) - 97] += 1
    print(*d)
    # file.write(' '.join(map(str, d)) + '\n')

    a = set(s)

    for i in range(1, n):
        d[i] += d[i - 1]
    d = [0] + d
    m = d[-1]

    l, r = Decimal(0), Decimal(1)
    for i in range(len(s)):
        nl = l + Decimal(r - l) * Decimal(d[ord(s[i]) - 97]) / Decimal(m)
        nr = l + Decimal(r - l) * Decimal(d[ord(s[i]) - 96]) / Decimal(m)
        l, r = nl, nr

    if l == 0:
        print(0)
        # file.write('0' + '\n\n')
    else:
        p = 1
        for c in range(1, 700):
            l *= Decimal(2)
            p *= 2
            if nl <= (Decimal(int(l)) + Decimal(1)) / Decimal(p) < r:
                print(bin(int(l) + 1)[2:].rjust(c, '0'))
                # file.write(bin(int(l) + 1)[2:].rjust(c, '0') + '\n\n')
                break
    print()
# file.close()
input()
