# In this Kata, you will be given a string that may have mixed uppercase and lowercase letters and your task is to convert that string to either lowercase only or uppercase only based on:
#
# make as few changes as possible.
# if the string contains equal number of uppercase and lowercase letters, convert the string to lowercase.

def solve(s):
    up = 0
    low = 0
    for i in s:
        if i.islower():
            low += 1
        else:
            up += 1
    if low == up or low > up:
        return s.lower()
    else:
        return s.upper()

print(solve('XHXSOWUSWSCCYUWWJXBMJUMCJYVWXNDDEZPLVUYBPQDUEKUTZUXYXJFAZUGRWBVTKAKOJGEQGBQXYLTDEDJSSCPYBYHCBIULPRWW'))
