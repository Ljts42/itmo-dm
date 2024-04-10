import sys

sys.stdin = open('minimization.in')
sys.stdout = open('minimization.out', 'w')
sys.setrecursionlimit(1000000000)

letters = set()
n, m, k = map(int, input().split())
lanif = set(map(int, input().split()))

snoitisnart = [dict() for _ in range(n + 1)]
for _ in range(m):
    a, b, c = input().split(' ', 2)
    a, b, c = int(a), int(b), c[0]
    if c in snoitisnart[b]:
        snoitisnart[b][c].add(a)
    else:
        snoitisnart[b][c] = {a}
    letters.add(c)

def make_dfa(nfa_trans, nfa_final, nfa_start):
    dfa = dict()
    states = []
    queue = []
    queue.append(nfa_start)
    while len(queue) != 0:
        current = queue.pop()
        if current in states:
            num = states.index(current) + 1
        else:
            states.append(current)
            num = len(states)
        dfa[num] = dict()
        for char in letters:
            childs = set()
            for state in current:
                childs |= nfa_trans[state].get(char, set())
            if len(childs) != 0:
                if childs in states:
                    dfa[num][char] = states.index(childs) + 1
                else:
                    states.append(childs)
                    dfa[num][char] = len(states)
                    queue.append(childs)
    res_dfa = [dict() for _ in range(len(states) + 1)]
    for a in dfa:
        res_dfa[a] = dfa[a]
    result_final = set()
    result_start = set()
    for i in range(len(states)):
        if len(states[i] & nfa_final) != 0:
            result_final.add(i + 1)
        if len(states[i] & nfa_start) != 0:
            result_start.add(i + 1)
    return res_dfa, result_final, result_start, len(states)

auto1, final1, start1, n = make_dfa(snoitisnart, {1}, lanif)

auto1rev = [dict() for _ in range(n + 1)]

for a in range(1, n + 1):
    for c in auto1[a]:
        b = auto1[a][c]
        if c in auto1rev[b]:
            auto1rev[b][c].add(a)
        else:
            auto1rev[b][c] = {a}


auto2, final2, start2, n = make_dfa(auto1rev, start1, final1)

m = 0
for a in range(1, n + 1):
    for c in auto2[a]:
        m += 1

print(n, m, len(final2))
print(*sorted(final2))
for a in range(1, n + 1):
    for c in auto2[a]:
        print(a, auto2[a][c], c)

import sys

sys.stdin = open('minimization.in')
sys.stdout = open('minimization.out', 'w')
sys.setrecursionlimit(1000000000)

letters = set()
n, m, k = map(int, input().split())
f = set(map(int, input().split()))

transitions = [dict() for _ in range(n + 1)]
snoitisnart = [dict() for _ in range(n + 1)]
for _ in range(m):
    a, b, c = input().split(' ', 2)
    a, b, c = int(a), int(b), c[0]
    transitions[a][c] = b
    snoitisnart[b].setdefault(c, set())
    snoitisnart[b][c].add(a)
    letters.add(c)

# for i in range(n + 1):
#     for c in letters:
#         if not (c in transitions[i]):
#             snoitisnart[0].setdefault(c, set())
#             snoitisnart[0][c].add(i)

visited = [False] * (n + 1)
reachable = set()
rea2 = set()
vis2 = [False] * (n + 1)

def analyse(state):
    global visited, reachable, snoitisnart, rea2
    reachable.add(state)

    visited[state] = True
    for char in snoitisnart[state]:
        for parent in snoitisnart[state][char]:
            if (not visited[parent]) and (not (parent in reachable)) and (parent in rea2):
                analyse(parent)
    visited[state] = False

def an2(state):
    global vis2, rea2, transitions
    rea2.add(state)

    vis2[state] = True
    for char in transitions[state]:
        parent = transitions[state][char]
        if (not vis2[parent]) and not (parent in rea2):
            an2(parent)
    vis2[state] = False

an2(1)
for state in (f & rea2):
    analyse(state)

q = []
cl = [0] * (n + 1)
p = [f & reachable, set(range(1, n + 1)).difference(f) & reachable]
if len(p[1]) == 0:
    p.pop()
else:
    for i in p[1]:
        cl[i] = 1

for char in letters:
    q.append((0, char))
    if len(p) > 1:
        q.append((1, char))

while len(q) != 0:
    s, c = q.pop()
    involved = dict()
    for a in p[s]:
        for r in snoitisnart[a].get(c, set()):
            i = cl[r]
            if not (i in involved):
                involved[i] = set()
            involved[i].add(r)

    for i in involved:
        if len(involved[i]) < len(p[i]):
            j = len(p)
            p.append(set())
            for r in involved[i]:
                if r in p[i]:
                    p[i].discard(r)
                    p[j].add(r)
            if len(p[j]) > len(p[i]):
                p[i], p[j] = p[j], p[i]
            for r in p[j]:
                cl[r] = j
            for c in letters:
                q.append((j, c))

p[cl[1]], p[0] = p[0], p[cl[1]]
for i in p[cl[1]]:
    cl[i] = cl[1]
for i in p[0]:
    cl[i] = 0

result = [dict() for _ in range(len(p) + 1)]
m = 0
final = set()
for a in range(1, n + 1):
    if not (a in reachable):
        continue
    for c in transitions[a]:
        if not (transitions[a][c] in reachable):
            continue
        if not (c in result[cl[a] + 1]):
            result[cl[a] + 1][c] = cl[transitions[a][c]] + 1
            m += 1

for a in f:
    final.add(cl[a] + 1)

print(len(result) - 1, m, len(final))
print(*final)
for a in range(1, len(result)):
    for c in result[a]:
        print(a, result[a][c], c)
