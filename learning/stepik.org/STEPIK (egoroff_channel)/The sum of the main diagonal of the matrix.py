n = int(input())
a = []

for i in range(n):
    a.append(list(map(int, input().split())))
s = 0
for i in range(n):
    for j in range(n):
        if i == j:
            s += a[i][j]
print(s)

