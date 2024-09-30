LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5


def main():
    birthdays = dict()
    choice = 0
    while choice != QUIT:
        choice = get_menu_choice()
        if choice == LOOK_UP:
            look_up(birthdays)
        elif choice == ADD:
            add(birthdays)
        elif choice == CHANGE:
            change(birthdays)
        elif choice == DELETE:
            delete(birthdays)
            
            
def get_menu_choice():
    print()
    print('Друзья и их дни рождения')
    print('-' * 15)
    print('1. Найти день рождения')
    print('2. Добавить новый день рождения')
    print('3. Изменить день рождения')
    print('4. Удалить день рождения')
    print('5. Выйти из программы')
    print()
    
    choice = int(input('Введите выбранный пункт: '))
    
    while choice < LOOK_UP or choice > QUIT:  # Пределы 
        choice = int(input('Введите выбранный пункт: '))
        
    return choice  # Вернуть выбор


def look_up(birthdays):
    name = input('Введите имя: ')  # Получить имя
    print(birthdays.get(name, 'Не найдено'))
    
    
def add(birthdays):
    name = input('Введите имя: ')
    bday = input('Введите день рождения: ')
    if name not in birthdays:
        birthdays[name] = bday
    else:
        print('Эта запись уже существует')
    
        
def change(birthdays):
    name = input('Введите имя: ')
    if name in birthdays:
        bday = input('Введите новый день рождения: ')
        birthdays[name] = bday
    else:
        print('Это имя не найдено.')
        

def delete(birthdays):
    name = input('Введите имя: ')
    if name in birthdays:
        del birthdays[name]
    else:
        print('Имя не найдено')
        
        
if __name__ == '__main__':
    main()    