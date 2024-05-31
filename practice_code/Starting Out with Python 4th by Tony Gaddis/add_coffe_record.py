# Эта программа добавляет записи о запасах кофе в файл coffee.txt
def main():
    # Создадим переменную для управления циклом
    another = 'yes'
    # Открыть файл coffee.txt в режиме дозаписи
    coffee_file = open('coffee.txt', 'a')
    # Добавить записи в файл
    while another == 'yes':
        # Получить данные с записью о кофе
        print('Введите следующие данные о кофе: ')
        description = input('Описание: ')
        quantity = int(input('Количество в фунтах: '))
        # Добавить данные в файл
        coffee_file.write(f'{description}\n')
        coffee_file.write(f'{quantity}\n')
        # Определить желает ли пользователь добавить в файл еще одну запись
        print('Желаете добавить еще одну запись? ')
        another = input('yes - если да, no - если нет: ')

    coffee_file.close()
    print('Данные добавлены в файл coffee.txt')


if __name__ == '__main__':
    main()
