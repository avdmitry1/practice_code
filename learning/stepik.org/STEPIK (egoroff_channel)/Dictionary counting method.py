s = input()
d = {}

for i in s.lower():
    if i.isalpha():
        if i in d:
            d[i] = d.get(i, 0) + 1
        else:
            d[i] = 1
print(d)