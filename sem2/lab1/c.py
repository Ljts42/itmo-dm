import sys

sys.stdin = open('problem3.in')
sys.stdout = open('problem3.out', 'w')
sys.setrecursionlimit(1000000)

n, m, k = map(int, input().split())
final = set(map(int, input().split()))

transitions = [dict() for _ in range(n + 1)]
snoitisnart = [set() for _ in range(n + 1)]
for _ in range(m):
    a, b, _ = input().split(' ', 2)
    a, b = int(a), int(b)
    if b in transitions[a]:
        transitions[a][b] += 1
    else:
        transitions[a][b] = 1
        snoitisnart[b].add(a)

visited = [False] * (n + 1)
reachable = set()

def analyse(state):
    global visited, reachable, snoitisnart

    reachable.add(state)

    visited[state] = True
    for parent in snoitisnart[state]:
        if not visited[parent] and not parent in reachable:
            analyse(parent)
    visited[state] = False


for state in final:
    analyse(state)


def check(state):
    global visited, reachable, transitions
    if visited[state]:
        return True
    
    visited[state] = True
    for available in transitions[state]:
        if available in reachable and check(available):
            return True
    visited[state] = False
    return False


tmp = 1
result = 0

def count(state):
    global transitions, visited, reachable, tmp, result
    
    if state in final:
        result += tmp

    visited[state] = True
    for available in transitions[state]:
        if not visited[available] and available in reachable:
            tmp *= transitions[state][available]
            count(available)
            tmp //= transitions[state][available]
    visited[state] = False

if check(1):
    print(-1)
else:
    count(1)
    print(result)
