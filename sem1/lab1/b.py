n = int(input())
res = [1] * 5
 
for _ in range(n):
    m, f = input().split()    
    m = int(m)
    f = list(map(int, list(f)))
 
    # 0 save
    if f[0] == 1:
        res[0] = 0
     
    # 1 save
    if f[-1] == 0:
        res[1] = 0
 
    # sd
    if m != 0:
        for i in range(2 ** (m - 1)):
            if f[i] == f[2 ** m - i - 1]:
                res[2] = 0
    else:
        res[2] = 0
 
    # m
    if res[3]:
        for i in range(2 ** m):
            for j in range(i + 1, 2 ** m):
                if f[i] <= f[j]:
                    continue
                 
                a = bin(i)[2:]
                b = bin(j)[2:]
                a = [0] * (m - len(a)) + list(map(int, list(a)))
                b = [0] * (m - len(b)) + list(map(int, list(b)))
                res[3] = 0
                for k in range(m):
                    if a[k] > b[k]:
                        res[3] = 1
                        break
                if not res[3]:
                    break
            if not res[3]:
                    break
 
    # l
    if res[4]:
        for i in range(2 ** m - 1, 0, -1):
            for j in range(i):
                f[j] = f[j] ^ f[j + 1]
            if f[0] == 1 and (bin(2 ** m - i)[2:]).count('1') > 1:
                res[4] = 0
                break
 
    if sum(res) == 0:
        break
 
if sum(res) == 0:
    print('YES')
else:
    print('NO')
