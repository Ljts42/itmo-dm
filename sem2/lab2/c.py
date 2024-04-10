import sys
  
sys.stdin = open('useless.in')
sys.stdout = open('useless.out', 'w')
 
n, start = input().split()
n = int(n)
rules = dict()
generative = set()
term = set(map(chr, range(97, 123)))
neterm = set()
neterm.add(start)
 
for _ in range(n):
    a = input()
    neterm.add(a[0])
    if not (a[0] in rules):
        rules[a[0]] = []
    if len(a) == 4:
        generative.add(a[0])
    else:
        a, b = a.split(' -> ')
        if len(term & set(b)) == len(set(b)):
            generative.add(a)
        rules[a].append(set(b))
        neterm |= set(b).difference(term)
 
changed = True
while changed:
    changed = False
    for i in rules:
        if i in generative:
            continue
        for j in rules[i]:
            check = True
            for k in j:
                if not ((k in generative) or (k in term)):
                    check = False
                    break
            if check:
                generative.add(i)
                changed = True
                break

extra = set()
for i in rules:
    if not (i in generative):
        extra.add(i)
        continue
    q = []
    for j in rules[i]:
        if len(j & (generative | term)) != len(j):
            q.append(j)
    for j in q:
        rules[i].remove(j)
    if len(rules[i]) == 0:
        extra.add(i)
 
for i in extra:
    rules.pop(i, None)
 
reachable = set()
if start in generative:
    reachable.add(start)
changed = True
while changed:
    changed = False
    for i in rules:
        if not (i in reachable):
            continue
        for j in rules[i]:
            for k in j:
                if k in term:
                    continue
                if not (k in reachable):
                    reachable.add(k)
                    changed = True
 
print(*sorted(neterm.difference(reachable)))