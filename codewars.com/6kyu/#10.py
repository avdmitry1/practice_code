def encode(st):
    new = ''
    vowels = {'a': '1', 'e': '2', 'i': '3', 'o': '4', 'u': '5'}
    for i in st:
        if i in vowels.keys():
            new += str(vowels.get(i))
        else:
            new += i
    return new
    
def decode(st):
    new2 = []
    vowels2 = {'1': 'a', '2': 'e', '3': 'i', '4': 'o', '5': 'u'}
    for i in st:
        if i in vowels2.keys():
            new2.append(vowels2[i])
        else:
            new2.append(i)
    return ''.join(new2)

print(decode('h2ll4'))
print(encode('hello'))