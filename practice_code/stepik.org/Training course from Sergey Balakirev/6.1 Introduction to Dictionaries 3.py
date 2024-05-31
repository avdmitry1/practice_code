# Data is entered in the key=value format in one line separated by a space.
# It is necessary to create a dictionary d based on them, then remove the keys 'False' and '3'
# from this dictionary, if they exist. The keys and values of a dictionary are strings.
# Display the resulting dictionary on the screen with the command:

words = input().split()
d = {}
for i in words:
    i = i.split('=')
    if i[0] not in 'False' and i[0] not in '3':
        d.setdefault(i[0], i[1])

print(*sorted(d.items()))