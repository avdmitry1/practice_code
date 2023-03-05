# Запись данных о сотрудниках в employee.txt

def main():
    num_emps = int(input('Сколько записей о сотрудниках ' +
                         'вы хотите создать? '))
    emp_file = open('employee.txt', 'w')
    for count in range(1, num_emps + 1):
        print(f'Введите данные о сотруднике № {count} ')
        name = input('Имя: ')
        id_num = int(input('Идентификационный номер: '))
        dept = input('Отдел: ')

        emp_file.write(f'{name}\n')
        emp_file.write(f'{id_num}\n')
        emp_file.write(f'{dept}\n')
        print()
    emp_file.close()
    print('Записи сотрудников сохранены в employee.txt')


if __name__ == '__main__':
    main()
