# input
n = int(input())
g1 = []
g2 = []
for i in range(n):
    g1.append(list(map(int, input().split())))
for i in range(n):
    g2.append(list(map(int, input().split())))
 
res = [[1] * 5, [1] * 5]
# check
for i in range(n):
    # refl
    if g1[i][i] == 0:
        res[0][0] = 0
    if g2[i][i] == 0:
        res[1][0] = 0
     
    # aref
    if g1[i][i] == 1:
        res[0][1] = 0
    if g2[i][i] == 1:
        res[1][1] = 0
 
    for j in range(i + 1, n):
        # simm
        if g1[i][j] != g1[j][i]:
            res[0][2] = 0
        if g2[i][j] != g2[j][i]:
            res[1][2] = 0
        # asim
        if g1[i][j] == g1[j][i] and g1[i][j] == 1:
            res[0][3] = 0
        if g2[i][j] == g2[j][i] and g2[i][j] == 1:
            res[1][3] = 0
         
        for k in range(j + 1, n):
            # tran
            if ((g1[i][j] * g1[j][k] == 1) and not g1[i][k]) or \
               ((g1[j][k] * g1[k][i] == 1) and not g1[j][i]) or \
               ((g1[k][i] * g1[i][j] == 1) and not g1[k][j]) or \
               ((g1[k][j] * g1[j][i] == 1) and not g1[k][i]) or \
               ((g1[i][k] * g1[k][j] == 1) and not g1[i][j]) or \
               ((g1[j][i] * g1[i][k] == 1) and not g1[j][k]):
                res[0][4] = 0
            if ((g2[i][j] * g2[j][k] == 1) and not g2[i][k]) or \
               ((g2[j][k] * g2[k][i] == 1) and not g2[j][i]) or \
               ((g2[k][i] * g2[i][j] == 1) and not g2[k][j]) or \
               ((g2[k][j] * g2[j][i] == 1) and not g2[k][i]) or \
               ((g2[i][k] * g2[k][j] == 1) and not g2[i][j]) or \
               ((g2[j][i] * g2[i][k] == 1) and not g2[j][k]):
                res[1][4] = 0
 
 
# output
print(*res[0])
print(*res[1])
for i in range(n):
    print(*[max([g1[i][k] * g2[k][j] for k in range(n)]) for j in range(n)])