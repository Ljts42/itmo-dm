from functools import cmp_to_key
def compare(lhs, rhs):
    print(1, lhs, rhs, flush=True)
    if input() == "YES":
        return -1
    return 1

n = int(input())
s = list(range(1, n + 1))
print(0, *sorted(s, key=cmp_to_key(compare)))
