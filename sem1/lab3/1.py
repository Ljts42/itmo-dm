n = int(input())
 
v = [0] * n
 
for i in range(2 ** n):
    print(*v, sep='')
    for j in range(n - 1, -1, -1):
        v[j] = (v[j] + 1) % 2
        if v[j] == 1:
            break
