def main():

    # Открыть файл для чтения
    infile = open('numbers.txt', 'r')

    # Прочитать три числа из файла
    num1 = int(infile.readline())
    num2 = int(infile.readline())
    num3 = int(infile.readline())

    # Закрыть файл
    infile.close()

    # Сложить три числа
    Total = num1 + num2 + num3

    # Показать числа и их сумму
    print(f'Числа: {num1}, {num2}, {num3}')
    print(f'Их сумма: {Total}')


if __name__ == '__main__':
    main()
