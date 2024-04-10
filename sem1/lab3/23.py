s = input()
n = len(s)
 
if int(s) == 0:
    print('-')
else:
    v = list(s)
    for j in range(n - 1, -1, -1):
        v[j] = (int(v[j]) + 1) % 2
        if int(v[j]) == 0:
            break
    print(*v, sep='')
 
if int(s, 2) + 1 == 2 ** n:
    print('-')
else:
    v = list(s)
    for j in range(n - 1, -1, -1):
        v[j] = (int(v[j]) + 1) % 2
        if int(v[j]) == 1:
            break
    print(*v, sep='')
