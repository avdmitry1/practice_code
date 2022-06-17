d = {}
n = int(input())
for key in range(n):
    name = input()
    if name not in d:
        print('OK')
        d[name] = 1
    else:
        print(f'{name}{d[name]}')
        d[name] += 1

