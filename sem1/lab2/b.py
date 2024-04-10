string = input()
shiftsTable = []
shiftsTable.append(string)
for _ in range(len(string) - 1):
    string = string[1:] + string[0]
    shiftsTable.append(string)
shiftsTable.sort()

result = ''
for line in shiftsTable:
    result += line[-1]
print(result)
