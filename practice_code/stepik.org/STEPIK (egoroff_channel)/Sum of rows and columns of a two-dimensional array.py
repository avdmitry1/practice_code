n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

for i in range(n):
    row = 0
    for j in range(m):
        row += a[i][j]
    print(row, end=' ')
print()
for i in range(m):
    column = 0
    for j in range(n):
        column += a[j][i]
    print(column, end=' ')

