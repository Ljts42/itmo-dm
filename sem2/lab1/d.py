import sys

sys.stdin = open('problem4.in')
sys.stdout = open('problem4.out', 'w')
sys.setrecursionlimit(1002)

n, m, k, l = map(int, input().split())
final = set(map(int, input().split()))

transitions = [dict() for _ in range(n + 1)]
for _ in range(m):
    a, b, _ = input().split(' ', 2)
    a, b = int(a), int(b)
    if b in transitions[a]:
        transitions[a][b] += 1
    else:
        transitions[a][b] = 1

queue = {1}
counts = [[0] * (n + 1) for _ in range(l + 1)]
counts[0][1] = 1
for i in range(l):
    available = set()
    for state in queue:
        for child in transitions[state]:
            counts[i + 1][child] += counts[i][state] * transitions[state][child]
            available.add(child)
    queue = available.copy()

result = 0
for state in final:
    result += counts[-1][state]

print(result % 1000000007)
