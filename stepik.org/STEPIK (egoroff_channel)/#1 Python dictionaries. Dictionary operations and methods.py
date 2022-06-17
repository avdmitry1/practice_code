number = int(input())
d = {}
for i in range(1, number + 1):
    d.setdefault(i, i ** 2)
print(d)
