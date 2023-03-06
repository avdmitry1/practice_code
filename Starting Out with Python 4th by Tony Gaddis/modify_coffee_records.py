# Эта программа позволяет пользователю изменять количество
# в записи файла coffee.txt
import os  # Этот модуль нужен для функций remove и rename


def main():

    found = False  # Создать булевую переменную в качестве флага
    # Получить искомое значение и количество
    search = input('Введите искомое описание: ')
    new_qty = input('Введите новое количество: ')
    coffee_file = open('coffee.txt', 'r')  # Открыть исходный файл coffee.txt
    temp_file = open('temp.txt', 'w')  # Открыть временный файл temp.txt
    descr = coffee_file.readline().rstrip('\n')  # Прочитать поле с первой записи
    while descr != '':  # Прочитать остаток
        qty = float(coffee_file.readline())  # Прочитать поле с количеством
        if descr == search:  # Записать во временый файл новую запись либо старую
            # Записать во временный файл измененную запись
            temp_file.write(f'{descr}\n')
            temp_file.write(f'{new_qty}\n')
            found = True  # Назначить флагу новое значение
        else:  # Записать исходную запись во временный файл
            temp_file.write(f'{descr}\n')
            temp_file.write(f'{qty}\n')
        descr = coffee_file.readline().rstrip('\n')  # Прочитать следующее описание
    coffee_file.close()  # Закрыть файл с данными о кофе и временный файл
    temp_file.close()
    os.remove('coffee.txt')  # Удалить исходный файл coffee.txt
    os.rename('temp.txt', 'coffee.txt')  # Переименновать временный файл
    # Если искомое значение в файле не найдено, показать сообщение
    print('Файл обновлен') if found else print('Это значение не найдено')


if __name__ == '__main__':
    main()
