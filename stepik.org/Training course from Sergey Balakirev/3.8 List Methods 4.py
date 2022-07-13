# In one line, a space is entered: first name, patronymic and last name. It is necessary to present these data
# as a new line in the format: Surname I.O. (For example, Sergey Mikhailovich Balakirev -> Balakirev S.M.).

name = input().split()

print(f'{name[2]} {name[0][0]}.{name[1][0]}.')
