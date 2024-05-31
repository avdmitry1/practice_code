a = []
row = 0
column = 0
for i in range(5):
    a.append(list(map(int, input().split())))

for i in range(5):
    for j in range(5):
        if a[i][j] == 1:
            row = i
            column = j
print(abs(2 - row) + abs(2 - column))