n, k = map(int, input().split())

for i in range(k ** n):
    for j in range(n):
        r = (i // (k ** j)) % (2 * k) - k
        print(k - 1 - abs(r + (r < 0)), end='')
    print()
