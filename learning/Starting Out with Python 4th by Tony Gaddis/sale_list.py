NUM_DAYS = 5


def main():
    sales = [0] * NUM_DAYS
    print('Введите продажи за каждый день.')

    for index in range(len(sales)):
        sales[index] = int(input(f'День № {index + 1}: '))

    print('Значения которые были введены: ')
    for value in sales:
        print(value)


if __name__ == '__main__':
    main()
