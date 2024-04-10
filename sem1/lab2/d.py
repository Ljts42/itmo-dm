string = input()
alphabet = list(range(1, 27))
result = []
for letter in string:
    result.append(alphabet[ord(letter) - 97])
    for i in range(26):
        if alphabet[i] < alphabet[ord(letter) - 97]:
            alphabet[i] += 1
    alphabet[ord(letter) - 97] = 1

print(*result)
