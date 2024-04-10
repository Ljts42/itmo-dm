n = int(input())
 
def gr2(x, s):
    if x == 1:
        return s
    l1 = list(map(lambda y: '0' + y, s))
    l2 = list(map(lambda y: '1' + y, reversed(s)))
    return gr2(x - 1, l1 + l2)
 
for i in gr2(n, ['0', '1']):
    print(i)
