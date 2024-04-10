string = input()
dictionary = {chr(i + 97): i for i in range(26)}
buffer = ''
reserved = 26
result = []

for letter in string:
    if buffer + letter in dictionary:
        buffer += letter
    else:
        result.append(dictionary[buffer])
        dictionary[buffer + letter] = reserved
        reserved += 1
        buffer = letter

result.append(dictionary[buffer])
print(*result)
