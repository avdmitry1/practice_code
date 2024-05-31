word = input()
result = ''
for i in word:
    if i not in result:
        result += i
print(result)