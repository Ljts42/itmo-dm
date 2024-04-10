n, k = map(int, input().split())
s = []
r = False
pos = [0] * n
neg = [0] * n
count = [0] * k
for i in range(k):
    s.append(list(map(int, input().split())))
    count[i] = s[-1].count(-1)
    if count[i] == n - 1:
        for j in range(n):
            if s[-1][j] == 1:
                pos[j] = 1
                break
            elif s[-1][j] == 0:
                neg[j] = 1
                break
 
if k == 1:
    print('NO')
else:
    for _ in range(n):
        for i in range(k):
            for j in range(n):
                if pos[j] * neg[j] == 1:
                    r = True
                    break
                elif s[i][j] != -1:
                    if s[i][j] == 0:
                        if pos[j]:
                            s[i][j] = -1
                            count[i] += 1
                        elif neg[j]:
                            break
                    else:
                        if pos[j]:
                            break
                        elif neg[j]:
                            s[i][j] = -1
                            count[i] += 1
                    if count[i] == n - 1:
                        for q in range(n):
                            if s[i][q] == 1:
                                pos[q] = 1
                                break
                            elif s[i][q] == 0:
                                neg[q] = 1
                                break
            if r:
                break
            if count[i] == n - 1:
                continue
        if r:
            break
 
    if r:
        print('YES')
    else:
        print('NO')