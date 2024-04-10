number = int(input())
frequency = sorted(map(int, input().split()), reverse=True)
result = 0
while len(frequency) != 1:
    min1 = frequency.pop()
    min2 = frequency.pop()
    frequency.append(min1 + min2)
    result += frequency[-1]
    frequency.sort(reverse=True)
print(result)

##########################################
# word: abacaba
# a: 4, b: 2, c: 1
#
#         abc
#        /   \
#       /     bc(3)
#      /     /  \
#     a(4)  b(2) c(1)
#
# result: 1 + 2 + 3 + 4 = 10
#
##########################################
