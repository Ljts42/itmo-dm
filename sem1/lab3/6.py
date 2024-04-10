n = int(input())
v = ['0'] * n
r = []
for i in range(2 ** n):
    s = ''.join(v)
    if '11' not in s:
        r.append(s)
    for j in range(n - 1, -1, -1):
        if v[j] == '1':
            v[j] = '0'
        else:
            v[j] = '1'
            break
 
print(len(r))
for i in r:
    print(i)
