# Программа показывает записи которые находятся в employee.txt
def main():
    # Открыть файл employee.txt
    emp_file = open('employee.txt', 'r')
    name = emp_file.readline().rstrip('\n')
    # Прочитать первую строку с именем участника
    while name != '':
        id_num = emp_file.readline().rstrip('\n')
        dept = emp_file.readline().rstrip('\n')
        print(f'Имя: {name}\nID: {id_num}\nОтдел: {dept}')
        print('-' * 30)
        name = emp_file.readline().rstrip('\n')
    emp_file.close()


if __name__ == '__main__':
    main()
