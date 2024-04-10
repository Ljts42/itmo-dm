n = int(input())
s = '0' * n
r = set()
for i in range(2 ** n):
    print(s)
    r.add(s)
    if s[1:] + '1' not in r:
        s = s[1:] + '1'
    elif s[1:] + '0' not in r:
        s = s[1:] + '0'
    else:
        break
