n = int(input())
func = [0] * (2 ** n)
param = []
neg = [0] * n
for i in range(2 ** n):
    a, b = input().split()
    func[int(a, 2)] = int(b)
    if b == '1':
        param.append(a)
        for i in range(n):
            if a[i] == '0':
                neg[i] = 1
 
if len(set(func)) == 1:
    if func[0] == 0:
        print(2 + n)
        print(1, 1)
        print(2, 1, n + 1)
    else:
        print(2 + n)
        print(1, 1)
        print(3, 1, n + 1)
else:
    res = []
    for i in range(n):
        if neg[i]:
            res.append([1, i + 1])
            neg[i] = len(res) + n
 
    for i in param:
        if i[0] == '1':
            a = 1
        else:
            a = neg[0]
        for j in range(1, n):
            if i[j] == '1':
                res.append([2, min(a, j + 1), max(a, j + 1)])
            else:
                res.append([2, min(a, neg[j]), max(a, neg[j])])
            a = n + len(res)
 
    a = 3 * n - neg.count(0) - 1
    res.append([3, a, a + n - 1])
    a += 2 * n - 2
    b = n + len(res)
    for i in range(len(param) - 2):
        res.append([3, a + i * (n - 1), b])
        b += 1
 
    print(len(res) + n)
    for i in res:
        print(*i)