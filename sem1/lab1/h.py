n = int(input())
res = '((A0|B0)|(A0|B0))'
for i in range(1, n):
    res = '((' + res + f'|((A{i}|A{i})|(B{i}|B{i})))|(A{i}|B{i}))'
print(res)