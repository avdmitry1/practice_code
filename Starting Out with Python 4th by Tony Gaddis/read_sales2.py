# Эта программа применяет цикл for для чтения всех значений с файла sales.txt
def main():
    # Открыть файл sales.txt для чтения
    sales_file = open('sales.txt', 'r')
    # Прочитать все строки из файла
    for i in sales_file:
        # Конвертировать строку в число с плавающей точкой
        amount = float(i)
        # Отформатировать и показать сумму
        print(f'{amount:.2f}')

    # Закрыть файл
    sales_file.close()


if __name__ == '__main__':
    main()
