# Эта программа предлагает пользователю ввести суммы продаж
# и записать их в файл sales.txt

def main():
    # Получить количество дней
    num_days = int(
        input('За какое количество дней вы располагаете продажами? '))

    # Открыть новый файл с именем sales.txt
    sales_file = open('sales.txt', 'w')

    # Получить суммы продаж за каждый день и записать их
    for count in range(1, num_days + 1):
        # Получить продажи за день
        sales = float(input(f'Введите продажи за день № {count}: '))
        # Записать сумму продаж в файл
        sales_file.write(f'{sales}\n')
    sales_file.close()


if __name__ == '__main__':
    main()
