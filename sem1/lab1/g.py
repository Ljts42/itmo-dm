n = int(input())
a = list(map(int, input().split()))
s = int(input())
 
res = ''
for i in range(n):
    if a[i] == s:
        res = i + 1
        break
if res != '':
    print(res)
elif len(bin(s)) > len(bin(max(a))):
    print('Impossible')
elif s == 0:
    print('~1&1')
else:
    m = len(bin(max(a, key=lambda x: len(bin(x))))) - 2
    b = []
    prov = ''
    for i in a:
        b.append(bin(i)[2:].rjust(m, '0'))
    # print(*b)
    s = bin(s)[2:].rjust(m, '0')
    # if s.count('1') <= s.count('0'):
    for i in range(m):
        if s[i] == '1':
            if res != '':
                res += '|'
                prov += '|'
            res += '('
            prov += '('
            for j in range(n):
                if b[j][i] == '0':
                    res += '~'
                    prov += '~'
                res += str(j + 1)
                prov += str(a[j])
                if j == n - 1:
                    res += ')'
                    prov += ')'
                else:
                    res += '&'
                    prov += '&'
 
    if res != '' and eval(prov) == int(s, 2):
        print(res)
    else:
        print('Impossible')