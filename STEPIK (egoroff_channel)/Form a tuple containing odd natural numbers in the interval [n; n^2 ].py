number = int(input())
result = []
for i in range(number, (number ** 2) + 1):
    if i % 2 != 0:
        result.append(i)
print(tuple(result))