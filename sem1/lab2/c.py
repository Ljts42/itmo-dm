string = input()
shiftsTable = [''] * len(string)
for _ in range(len(string)):
    for i in range(len(string)):
        shiftsTable[i] = string[i] + shiftsTable[i]
    shiftsTable.sort()

print(shiftsTable[0])
