from string import ascii_lowercase
alphabet = {}
a = 1
for i in ascii_lowercase:
    alphabet.setdefault(i, a)
    a += 1
for key, item in alphabet.items():
    print(key, item)