word = list(map(str, input().split()))


result = list(map(lambda x: (x.upper(), x.lower()), word))
print(result)