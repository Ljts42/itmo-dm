import sys

sys.stdin = open('problem5.in')
sys.stdout = open('problem5.out', 'w')
sys.setrecursionlimit(1002)

n, m, k, l = map(int, input().split())
final = set(map(int, input().split()))

letters = set()
nfa = [dict() for _ in range(n + 1)]
for _ in range(m):
    a, b, c = input().split(' ', 2)
    a, b, c = int(a), int(b), c[0]
    if c in nfa[a]:
        nfa[a][c].add(b)
    else:
        nfa[a][c] = {b}
    letters.add(c)

dfa = dict()
states = []
queue = [{1}]
while len(queue) != 0:
    current = queue.pop()
    if current in states:
        num = states.index(current)
    else:
        states.append(current)
        num = len(states) - 1
    dfa[num] = dict()
    for char in letters:
        childs = set()
        for state in current:
            childs |= nfa[state].get(char, set())
        if len(childs) != 0:
            if childs in states:
                dfa[num][char] = states.index(childs)
            else:
                states.append(childs)
                dfa[num][char] = len(states) - 1
                queue.append(childs)

transitions = [dict() for _ in range(len(states) + 1)]
for i in dfa:
    for c in dfa[i]:
        if dfa[i][c] + 1 in transitions[i + 1]:
            transitions[i + 1][dfa[i][c] + 1] += 1
        else:
            transitions[i + 1][dfa[i][c] + 1] = 1

lanif = set()
for i in range(len(states)):
    if len(states[i] & final) != 0:
        lanif.add(i + 1)

n = len(states)
counts = [[0] * (n + 1) for _ in range(l + 1)]
counts[0][1] = 1
queue = {1}
for i in range(l):
    available = set()
    for state in queue:
        for child in transitions[state]:
            counts[i + 1][child] += counts[i][state] * transitions[state][child]
            available.add(child)
    queue = available.copy()

result = 0
for state in lanif:
    result += counts[-1][state]

print(result % 1000000007)
