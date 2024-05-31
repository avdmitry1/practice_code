# Эта программа показывает записи из файла coffee.txt
def main():
    # Окрыть файл coffee.txt
    coffee_file = open('coffee.txt', 'r')
    # Прочитать поле с описанием первой записи
    description = coffee_file.readline().rstrip('\n')
    while description != '':
        quantity = float(coffee_file.readline())
        print(f'Описание: {description}\nКоличество: {quantity}')
        # Прочитать следующее описание
        description = coffee_file.readline().rstrip('\n')
    coffee_file.close()


if __name__ == '__main__':
    main()
