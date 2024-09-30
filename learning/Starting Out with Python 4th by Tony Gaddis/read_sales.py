# Эта программа читает все значения из файла sales.txt
def main():
    # Открыть файл для чтения sales.txt
    sales_file = open('sales.txt', 'r')
    # Прочитать первую строку не конвертируя в число
    # проверка на пустое строковое значение
    line = sales_file.readline()
    # Продолжать проверку до тех пор, пока из readline не будет возвращена пустая строка
    while line != '':
        # Конвертировать строку в число с плавающей точкой
        amount = float(line)
        # Отформатировать и показать сумму
        print(f'{amount:.2f}')
        # Прочитать следующую строку
        line = sales_file.readline()
    # Закрыть файл
    sales_file.close()


if __name__ == '__main__':
    main()
