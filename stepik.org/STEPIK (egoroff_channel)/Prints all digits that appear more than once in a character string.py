a = input()
b = ""
for i in a:
    if i.isdigit():
        if a.count(i) > 1:
            b += i
b = sorted(list(set(b)))
print(' '.join(b) if len(b) > 0 else 'NO')
