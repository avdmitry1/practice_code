# Эта программа позволяет пользователю изменять количество
# в записи файла coffee.txt
import os  # Этот модуль нужен для функций remove и rename


def main():
    # Создать булевую переменную в качестве флага
    found = False
    # Получить искомое значение и количество
    search = input('Введите искомое описание: ')
    new_qty = input('Введите новое количество: ')
    # Открыть исходный файл coffee.txt
    coffee_file = open('coffee.txt', 'r')
    # Открыть временный файл temp.txt
    temp_file = open('temp.txt', 'w')
    # Прочитать поле с первой записи
    descr = coffee_file.readline().rstrip('\n')
    # Прочитать остаток
    while descr != '':
        # Прочитать поле с количеством
        qty = float(coffee_file.readline())
        # Записать во временый файл новую запись либо старую
        if descr == search:
            # Записать во временный файл измененную запись
            temp_file.write(f'{descr}\n')
            temp_file.write(f'{new_qty}\n')
            # Назначить флагу новое значение
            found = True
        else:
            # Записать исходную запись во временный файл
            temp_file.write(f'{descr}\n')
            temp_file.write(f'{qty}\n')
        # Прочитать следующее описание
        descr = coffee_file.readline().rstrip('\n')
    # Закрыть файл с данными о кофе и временный файл
    coffee_file.close()
    temp_file.close()
    # Удалить исходный файл coffee.txt
    os.remove('coffee.txt')
    # Переименновать временный файл
    os.rename('temp.txt', 'coffee.txt')
    # Если искомое значение в файле не найдено, показать сообщение
    print('Файл обновлен') if found else print('Это значение не найдено')


if __name__ == '__main__':
    main()
