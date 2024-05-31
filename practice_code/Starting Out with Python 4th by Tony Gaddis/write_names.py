# Эта программа получает от пользователя три именни и пишет их в файл
def main():
    # Получить три именни
    print('Введите именна трёх друзей.')
    name1 = input('Друг № 1: ')
    name2 = input('Друг № 2: ')
    name3 = input('Друг № 3: ')

    # Открыть файл с именем friends.txt.
    my_file = open('friends.txt', 'w')

    # Записать именна в файл
    my_file.write(name1 + '\n')
    my_file.write(name2 + '\n')
    my_file.write(name3 + '\n')

    # Закрыть файл
    my_file.close
    print('Именна записаны в файл friends.txt')


if __name__ == '__main__':
    main()
