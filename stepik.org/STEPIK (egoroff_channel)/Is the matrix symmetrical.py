a = []
n = int(input())
count = 0
for i in range(n):
    a.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if a[i][j] != a[j][i]:
            count += 1
if count > 0:
    print('No')
else:
    print('Yes')