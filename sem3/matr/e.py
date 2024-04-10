import sys, queue

sys.stdin = open('cycles.in', 'r')
sys.stdout = open('cycles.out', 'w')

n, m = map(int, input().split())
w = list(map(int, input().split()))
s = set()
for _ in range(m):
    a = list(map(int, input().split()[1:]))
    b = 0
    for i in a:
        b += 1 << (i - 1)
    s.add(b)

q = list(s)
while q:
    i = q.pop()
    for j in range(n):
        k = i | (1 << j)
        if not k in s:
            q.append(k)
            s.add(k)
t = 0
r = 0
for i in range((1 << n) - 1, -1, -1):
    if not i in s:
        z = 0
        for j in range(n):
            

        # if bin(i).count('1') > z:
        #     z = bin(i).count('1')
        #     r = sum(map(lambda x: w[x] * (bin(i)[len(bin(i)) - x - 1] == '1'), range(len(bin(i)) - 2)))
        # else:
        #     r = max(r, sum(map(lambda x: w[x] * (bin(i)[len(bin(i)) - x - 1] == '1'), range(len(bin(i)) - 2))))
print(r)
