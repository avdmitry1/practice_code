comments = {
    'Дили': set(),
    'Били': set(),
    'Вили': set(),
}
a = input()
while a != 'конец':
    name, comment = a.split(': ')
    comments[name].add(comment)
    a = input()
for k, v in sorted(comments.items(), key=lambda item: - len(item[1])):
    print(f"Количество уникальных комментаторов у {k} - {len(v)}")
