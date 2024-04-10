import sys

sys.stdin = open('problem2.in')
sys.stdout = open('problem2.out', 'w')

word = input()
n, m, k = map(int, input().split())
final = set(map(int, input().split()))

transitions = [dict() for _ in range(n + 1)]
for _ in range(m):
    a, b, c = input().split(' ', 2)
    a, b, c = int(a), int(b), c[0]
    if c in transitions[a]:
        transitions[a][c].add(b)
    else:
        transitions[a][c] = {b}

queue = {1}
for char in word:
    available = set()
    for state in queue:
        if char in transitions[state]:
            available |= transitions[state][char]
    queue = available.copy()


if len(queue & final) != 0:
    print('Accepts')
else:
    print('Rejects')
