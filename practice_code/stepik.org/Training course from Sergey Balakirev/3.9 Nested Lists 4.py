# 3.9 Nested Lists 3
# It is necessary to implement a check for the presence of the entered word in this list. The result (True or False)
# is displayed on the screen. It is necessary to solve the problem without using a conditional operator

t = [["Скажи-ка", "дядя", "ведь", "не", "даром"],
    ["Я", "Python", "выучил", "с", "каналом"],
    ["Балакирев", "что", "раздавал?"]]
name = 'дядя'

print(name in str(t))