number = int(input())
string = list(map(int, input().split()))

dictionary = {i: chr(i + 97) for i in range(26)}
reserved = 27

result = dictionary[string[0]]
dictionary[reserved - 1] = result

for code in string[1:]:
    dictionary[reserved - 1] += dictionary[code][0]
    dictionary[reserved] = dictionary[code]
    reserved += 1
    result += dictionary[code]

print(result)
