import sys
sys.stdin = open('schedule.in', 'r')
sys.stdout = open('schedule.out', 'w')
n = int(input())
s = []
for _ in range(n):
    s.append(list(map(int, input().split())))
s.sort(key=lambda x: (-x[1], x[0]))
z = [-1] * n
p = 0
for i in range(n):
    for j in range(min(n, s[i][0]) - 1, -1, -1):
        if j == 0 and z[j] != -1:
            p += s[i][1]
            break
        elif z[j] == -1:
            z[j] = s[i][1]
            break
print(p)
