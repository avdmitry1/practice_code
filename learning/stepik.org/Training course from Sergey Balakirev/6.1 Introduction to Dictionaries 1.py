# The input of the program receives data in the form of a set of strings in the format:
#
# key1=value1
# key2=value2
# ...
# keyN=valueN
#
# The keys here are integers (see the example below). It is necessary to convert them into a dictionary d (without using the dict() function) and display it on the screen with the command:
#
# print(*sorted(d.items()))


s = input().split()
d = {}
for i in s:
    i = i.split('=')
    d.setdefault(int(i[0]), i[1])

print(*sorted(d.items()))
