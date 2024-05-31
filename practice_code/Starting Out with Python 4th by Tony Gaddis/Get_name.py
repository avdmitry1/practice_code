def get_name():
    # Получить имя и фамилию пользователя
    first = input('Введите свое имя: ')
    last = input('Введите свою фамилию : ')
    # Вернуть оба значения
    return first, last


first_name, last_name = get_name()

print(first_name, last_name)
