# You need to create a dictionary d where the keys will be names and the values will be a list of
# phone numbers for that name. Please note that one name can guard  different numbers.
# The resulting dictionary results in the command:
# print(*sorted(d.items()))
# P. S. To read the list of frequencies in the program, the initial lines have already been found.

lst_in = ['+71234567890 Сергей', '+71234567810 Сергей', '+51234567890 Михаил', '+72134567890 Николай']
d = {}

for i in lst_in:
    d.setdefault(i[13:], []).append(i[:12])

print(*sorted(d.items()))