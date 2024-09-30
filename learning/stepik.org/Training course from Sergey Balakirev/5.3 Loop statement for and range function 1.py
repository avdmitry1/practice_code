cities = list(map(str, input().split()))
first = []
last = []

for i, v in enumerate(cities):
    last.append(v[-1]) if v[-1] not in ['ь', 'ъ', 'ы'] else last.append(v[-2])
    first.append(v[0].lower())
print('ДА') if ''.join(first[1:]) == ''.join(last[:-1]) else print('НЕТ')