import sys
 
sys.stdin = open('epsilon.in')
sys.stdout = open('epsilon.out', 'w')

n, start = input().split()
n = int(n)
rules = dict()
epsilon = set()
term = set(map(chr, range(97, 123)))

for _ in range(n):
    a = input()
    if a[0] in epsilon:
        continue

    if len(a) == 4:
        epsilon.add(a[0])
    else:
        a, b = a.split(' -> ')
        if len(term & set(b)) > 0:
            continue
        if not (a in rules):
            rules[a] = []
        rules[a].append(set(b))

changed = True
while changed:
    changed = False
    for i in rules:
        if i in epsilon:
            continue
        for j in rules[i]:
            check = True
            for k in j:
                if not (k in epsilon):
                    check = False
                    break
            if check:
                epsilon.add(i)
                changed = True
                break

print(*sorted(epsilon))
'''
2 S
S -> aA
A -> b
ab

6 S
S -> TbS
S -> T
T -> FcT
T -> F
F -> dSd
F -> a
dabad

8 S
S -> aXbX
S -> aZ
X -> aY
X -> bY
X ->
Y -> X
Y -> cc
Z -> ZX
abc
'''