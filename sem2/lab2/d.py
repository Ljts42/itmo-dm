import sys
 
sys.stdin = open('nfc.in')
sys.stdout = open('nfc.out', 'w')

n, start = input().split()
n = int(n)
neterm = dict()
rules = set()
neterm.setdefault(start, set())

for _ in range(n):
    a = input()
    neterm.setdefault(a[0], set())
    if len(a) == 6:
        neterm[a[0]].add(a[5])
    else:
        rules.add(a[0] + a[-2:])
        neterm.setdefault(a[5], set())
        neterm.setdefault(a[6], set())

word = input()
m = len(word)

cnt = dict()
for c in neterm:
    cnt[c] = [[0] * m for _ in range(m)]

for c in neterm:
    for length in range(m):
        pos = length
        cnt[c][length][pos] = word[pos] in neterm[c]

for length in range(1, m):
    for pos in range(length - 1, -1, -1):
        for rule in rules:
            for i in range(pos, length):
                cnt[rule[0]][length][pos] += cnt[rule[1]][i][pos] * cnt[rule[2]][length][i + 1]

print(cnt[start][-1][0] % 1000000007)
