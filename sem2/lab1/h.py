import sys

sys.stdin = open('minimization.in')
sys.stdout = open('minimization.out', 'w')
sys.setrecursionlimit(1000000000)

n, m, k = map(int, input().split())
Q = set(range(1, n + 1))
F = set(map(int, input().split()))
L = set()
S = []
R = []

Aut = [dict() for _ in range(n + 1)]
Inv = [dict() for _ in range(n + 1)]
for _ in range(m):
    a, b, c = input().split(' ', 2)
    a, b, c = int(a), int(b), c[0]
    Aut[a][c] = b
    Inv[b].setdefault(c, set())
    Inv[b][c].add(a)
    L.add(c)

visited = [False] * (n + 1)
reachable = set()
rea2 = set()
vis2 = [False] * (n + 1)

def analyse(state):
    global visited, reachable, Inv, rea2
    reachable.add(state)

    visited[state] = True
    for char in Inv[state]:
        for parent in Inv[state][char]:
            if (not visited[parent]) and (not (parent in reachable)) and (parent in rea2):
                analyse(parent)
    visited[state] = False

def an2(state):
    global vis2, rea2, Aut
    rea2.add(state)

    vis2[state] = True
    for char in Aut[state]:
        parent = Aut[state][char]
        if (not vis2[parent]) and not (parent in rea2):
            an2(parent)
    vis2[state] = False

an2(1)
for state in (F & rea2):
    analyse(state)


Class = [0] * (n + 1)
Queue = []
P = [F.intersection(reachable),
    (Q.difference(F)).intersection(reachable)]
# if len(P[1]) == 0:
#     P.pop()
# else:
for i in P[1]:
    Class[i] = 1

for char in L:
    Queue.append([0, char])
    # if len(P) > 1:
    Queue.append([1, char])

while len(Queue) != 0:
    C, a = Queue.pop()
    Involved = dict()
    for q in P[C]:
        for r in Inv[q].get(a, set()):
            i = Class[r] + 0
            # if not (i in Involved):
            #     Involved[i] = set()
            Involved.setdefault(i, set())
            Involved[i].add(r)

    for i in Involved:
        if len(Involved[i]) < len(P[i]):
            j = len(P)
            P.append(set())
            for r in Involved[i]:
                # if r in P[i]:
                P[i].discard(r)
                P[j].add(r)
            if len(P[j]) > len(P[i]):
                P[i], P[j] = P[j], P[i]
            for r in P[j]:
                Class[r] = j + 0
            for c in L:
                Queue.append([j, c])

P[Class[1]], P[0] = P[0], P[Class[1]]
for i in P[Class[1]]:
    Class[i] = Class[1] + 0
for i in P[0]:
    Class[i] = 0

if max(Class) + 1 > len(P):
    while True:
        pass

rem = 0
for i in range(len(P)):
    if len(P[i]) == 0:
        del P[i]
        for j in range(len(Class)):
            if Class[j] >= i:
                Class[j] -= 1
# for _ in range(rem):
# while set() in P:
#     P.remove(set())

result = [dict() for _ in range(len(P) + 1)]
m = 0
newQ = set()
final = set()

g = set()
for a in range(1, n + 1):
    if not (a in reachable):
        continue
    for c in Aut[a]:
        if not (Aut[a][c] in reachable):
            continue
        if not (c in result[Class[a] + 1]):
            result[Class[a] + 1][c] = Class[Aut[a][c]] + 1
            m += 1
            newQ.add(Class[a] + 1)
            newQ.add(Class[Aut[a][c]] + 1)
            g.add(str(Class[a] + 1) + ' ' + str(Class[Aut[a][c]] + 1) + ' ' + c)

for a in F:
    if (Class[a] + 1) in newQ:
        final.add(Class[a] + 1)

# print(len(newQ), m, len(final))
print(len(newQ), len(g), len(final))
print(*final)
for i in sorted(g):
    print(i)
# if max(Class) + 1 > len(P):
#     while True:
#         pass
# minQ = 9999
# maxQ = -9999
# for a in range(1, len(result)):
#     for c in result[a]:
#         print(a, result[a][c], c)
#         minQ = min([a, minQ, result[a][c]])
#         maxQ = max([a, maxQ, result[a][c]])
# if minQ != 1:
#     while True:
#         pass
