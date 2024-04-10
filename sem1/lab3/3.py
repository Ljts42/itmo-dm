def agr3(x, n):
    r = ''
    while x > 0 or r == '':
        r = str(x % 3) + r
        x //= 3
    return '0' * (n - len(r) - 1) + r
 
def inc(x):
    r = ''
    for i in x:
        r += str((int(i) + 1) % 3)
    return r
 
n = int(input())
if n == 1:
    print('0\n1\n2')
else:
    for i in range(3 ** (n - 1)):
        print('0' + agr3(i, n))
        print('1' + inc(agr3(i, n)))
        print('2' + inc(inc(agr3(i, n))))
