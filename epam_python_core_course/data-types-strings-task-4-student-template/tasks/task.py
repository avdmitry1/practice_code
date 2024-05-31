import math
def check_str(s: str):
    alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789'
    word = ''
    for i in s:
        if i in alpha:
            word += i.lower()
    first = len(word) / 2
    return word[:math.ceil(first)] == word[int(first):][::-1]

print(check_str('32635745'))