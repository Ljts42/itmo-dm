import sys

sys.stdin = open('cf.in')
sys.stdout = open('cf.out', 'w')

## base inp
n, start = input().split()
n = int(n)
inp = set()

for _ in range(n):
    a = input()
    inp.add(a[0] + a[5:])

word = input()
w = set(word)
m = len(word)
k = ord(max(w)) + 1

rules = set()
term = set(map(chr, range(97, 123)))
neterm = dict()
neterm.setdefault(start, set())
epsilon = set()

## (forall 1 <= |rule| <= 2) & base find epsilon
for rule in inp:
    if len((set(rule) & term).difference(w)) == 0:
        neterm.setdefault(rule[0], set())
        if len(rule) > 3:
            rules.add(rule[:2] + chr(k))
            neterm.setdefault(chr(k), set())
            
            for i in range(2, len(rule) - 2):
                rules.add(chr(k) + rule[i] + chr(k + 1))
                neterm.setdefault(chr(k + 1), set())
                k += 1
            a, b = rule[-2:]
            rules.add(chr(k) + a + b)
            k += 1

            for i in rule:
                neterm.setdefault(i, set())
        elif len(rule) == 1:
            epsilon.add(rule)
        elif len(rule) == 2 and rule[1] in w:
            neterm[rule[0]].add(rule[1])
        else:
            rules.add(rule)
            for i in rule:
                neterm.setdefault(i, set())

for r in rules:
    for i in r:
        if i in w:
            neterm.setdefault(i, set())
            neterm[i].add(i)

## find eps
changed = True
while changed:
    changed = False
    for rule in rules:
        if rule[0] in epsilon:
            continue
        if len(set(rule[1:]).difference(epsilon)) == 0:
            epsilon.add(rule[0])
            changed = True

## del eps & base find chain
chain = dict()
for rule in rules.copy():
    if len(rule) == 2:
        chain.setdefault(rule[0], set())
        chain[rule[0]].add(rule[1])
    else:
        if rule[1] in epsilon:
            if rule[2] in epsilon:
                rules.add(rule[:2])
                rules.add(rule[::2])
                
                chain.setdefault(rule[0], set())
                chain[rule[0]].add(rule[1])
                chain[rule[0]].add(rule[2])
            else:
                if rule[2] in w:
                    neterm[rule[0]].add(rule[2])
                else:
                    rules.add(rule[::2])

                    chain.setdefault(rule[0], set())
                    chain[rule[0]].add(rule[2])
        else:
            if rule[2] in epsilon:
                if rule[1] in w:
                    neterm[rule[0]].add(rule[1])
                else:
                    rules.add(rule[:2])
                    
                    chain.setdefault(rule[0], set())
                    chain[rule[0]].add(rule[1])

## find chain
changed = True
while changed:
    changed = False
    for i in chain:
        for j in chain[i].copy():
            if j in chain:
                if len(chain[j].difference(chain[i])) > 0:
                    changed = True
                chain[i] |= chain[j]

## del chain
for rule in rules.copy():
    for i in chain:
        if rule[0] in chain[i]:
            rules.add(i + rule[1:])
for i in chain:
    for j in chain[i]:
        neterm[i] |= neterm[j]
for i in chain:
    for j in chain[i]:
        rules.discard(i + j)

## find generative
generative = set()
for i in neterm:
    if len(neterm[i]) != 0:
        generative.add(i)

changed = True
while changed:
    changed = False
    for rule in rules:
        if rule[0] in generative:
            continue
        if len(set(rule[1:]).difference(generative | w)) == 0:
            generative.add(rule[0])
            changed = True

## del generative
for rule in rules.copy():
    if not (rule[0] in generative):
        rules.discard(rule)
        continue

    if len(set(rule[1:]).difference(generative | w)) != 0:
        rules.discard(rule)

## count
cnt = dict()
for c in neterm:
    cnt[c] = [[False] * m for _ in range(m)]

for c in neterm:
    for length in range(m):
        pos = length
        cnt[c][length][pos] = word[pos] in neterm[c]

for length in range(1, m):
    for pos in range(length - 1, -1, -1):
        for rule in rules:
            for i in range(pos, length):
                cnt[rule[0]][length][pos] |= cnt[rule[1]][i][pos] & cnt[rule[2]][length][i + 1]

if cnt[start][-1][0]:
    print('yes')
else:
    print('no')
