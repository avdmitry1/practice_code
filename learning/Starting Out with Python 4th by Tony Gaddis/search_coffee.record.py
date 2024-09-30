# Программа по поиску записей файла coffee.txt
def main():
    # Создаем булевую переменную в качестве флага
    found = False
    search = input('Получить искомое описание: ')
    print('-' * 30)
    # Открыть файл coffee.txt
    coffee_file = open('coffee.txt', 'r')
    # Прочитать после с описанием кофе первой записи
    descr = coffee_file.readline().rstrip('\n')
    # Прочитать остаток файла
    while descr != '':
        qty = float(coffee_file.readline())
        # Определить соответствует ли запись поиску
        if descr == search:
            # Показать запись
            print(f'Описание: {descr}')
            print(f'Количество: {qty}')
            print('-' * 30)
            # Назначит флагу значение True
            found = True
        # Прочитать следующее описание
        descr = coffee_file.readline().rstrip('\n')
    coffee_file.close()
    # Если значение не найдено показать сообщение
    if not found:
        print('Это значение в файле не найдено')


if __name__ == '__main__':
    main()
