from string import *
word = input()
if len(set(word.lower())) == len(ascii_lowercase):
    print('YES')
else:
    print('NO')
