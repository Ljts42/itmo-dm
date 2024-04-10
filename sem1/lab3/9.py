n = int(input())

def psp(n, k=0, p=''):
    if len(p) == 2 * n:
        print(p)
        return

    if k < n:
        psp(n, k + 1, p + '(')

    if len(p) < 2 * k:
        psp(n, k, p + ')')

psp(n)