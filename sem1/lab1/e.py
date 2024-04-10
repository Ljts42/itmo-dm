n = int(input())
func = [0] * (2 ** n)
param = []
for i in range(2 ** n):
    a, b = input().split()
    func[int(a, 2)] = int(b)
    param.append(a)
 
result = [func[0]]
for i in range(2 ** n - 1, 0, -1):
    for j in range(i):
        func[j] = func[j] ^ func[j + 1]
    result.append(func[0])
 
for i in range(2 ** n):
    print(param[i], result[i])