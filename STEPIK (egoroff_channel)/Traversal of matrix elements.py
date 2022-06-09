n = int(input())
a = []

for i in range(n):
    a.append(list(map(int, input().split())))
s = 0
for i in range(n):
    print()
    for j in range(n):
        print(a[j][i], end=' ')