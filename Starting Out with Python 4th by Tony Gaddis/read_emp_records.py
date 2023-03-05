# Программа показывает записи которые находятся в employee.txt
def main():
    # Открыть файл employee.txt
    emp_file = open('employee.txt', 'r')
    # Прочитать первую строку с именем участника
    for i in emp_file:
        print(i)
    emp_file.close()


if __name__ == '__main__':
    main()
