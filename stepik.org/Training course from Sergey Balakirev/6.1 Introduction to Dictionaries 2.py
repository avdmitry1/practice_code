# Data is entered in the key=value format in one line separated by a space.
# It is necessary to create a dictionary based on them, then check if there are keys with values:
#     'house', 'True' and '5' (all keys are strings). If they all exist, then display YES, otherwise - NO.


words = input().split()
d = {}
for i in words:
    i = i.split('=')
    d.setdefault(i[0], i[1])

print('ДА') if 'house' in d.keys() and 'True' in d.keys() and '5' in d.keys() else print('НЕТ')

