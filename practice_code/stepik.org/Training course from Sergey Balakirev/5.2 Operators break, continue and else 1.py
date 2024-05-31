# Book titles are entered (each on a new line). Remove from the entered list all names consisting of two or more words
# (words in the names are separated by a space). Display the result on the screen as a string of the remaining names
# separated by a space.


lst_in = [
    'Муму',
    'Евгений Онегин',
    'Сияние',
    'Мастер и Маргарита',
    'Пиковая дама',
    "Колобок",
]
a_list = []
while lst_in:
    word = lst_in.pop(0)
    a_list.append(word) if ' ' not in word else word
print(a_list)
