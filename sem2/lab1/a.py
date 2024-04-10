import sys

sys.stdin = open('problem1.in')
sys.stdout = open('problem1.out', 'w')

word = input()
n, m, k = map(int, input().split())
final = set(map(int, input().split()))

transitions = [dict() for _ in range(n + 1)]
for _ in range(m):
    a, b, c = input().split(' ', 2)
    a, b, c = int(a), int(b), c[0]
    transitions[a][c] = b

state = 1
for char in word:
    if char in transitions[state]:
        state = transitions[state][char]
    else:
        state = -1
        break
 
if state in final:
    print('Accepts')
else:
    print('Rejects')


# Earth = [1.4960e+11, 0.0000e+00, 0.0000e+00, 2.9800e+04, 5.9740e+24]
# Mars = [2.2790e+11, 0.0000e+00, 0.0000e+00, 2.4100e+04, 6.4190e+23]
# Mercury = [5.7900e+10, 0.0000e+00, 0.0000e+00, 4.7900e+04, 3.3020e+23]
# Sun = [0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 1.9890e+30]
# Venus = [1.0820e+11, 0.0000e+00, 0.0000e+00, 3.5000e+04, 4.8690e+24]
