import sys
 
sys.stdin = open('automaton.in')
sys.stdout = open('automaton.out', 'w')

n, start = input().split()
n = int(n)

transitions = dict()
pp = [[set() for i in range(26)] for j in range(26)]
for _ in range(n):
    a, b = input().split(' -> ')
    if len(b) == 2:
        b, c = b[0], b[1]
    else:
        b, c = b[0], ''

    if not (a in transitions):
        transitions[a] = dict()
    if not (c in transitions):
        transitions[c] = dict()

    if not (b in transitions[a]):
        transitions[a][b] = set()
    transitions[a][b].add(c)
    pp[ord(a) - 65][ord(b) - 97].add(c)

def check(word):
    global transitions, start
    prev = {start[0]}
    for char in word:
        cur = set()
        for state in prev:
            if char in transitions.get(state, dict()):
                cur |= transitions[state][char]
        if len(cur) == 0:
            return 'no'
        prev = cur.copy()
    if '' in prev:
        return 'yes'
    return 'no'

def check2(word):
    q = set()
    q.add(start)
    for c in word:
        q2 = set()
        for s in q:
            q2 |= pp[ord(s) - 65][ord(c) - 97]
        print(q2)
        if len(q2) == 0:
            return False
        q = q2.copy()
    if '0' in q:
        return False
    return True

m = int(input())
for _ in range(m):
    print(check2(input()))
