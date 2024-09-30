import contact
import pickle

LOOK_UP, ADD, CHANGE, DELETE, QUIT = 1, 2, 3, 4, 5
FILENAME = 'contacts.dat'
def main():
    mycontacts = load_contacts()
    choice = 0
    while choice != QUIT:
        choice = get_menu_choice()
        if choice == LOOK_UP:
            look_up(mycontacts)
        elif choice == ADD:
            add(mycontacts)
        elif choice == CHANGE:
            change(mycontacts)
        elif choice == DELETE:
            delete(mycontacts)
    save_contacts(mycontacts)


def load_contacts():
    try:
        input_file = open(FILENAME, 'rb')
        contacts_dict = pickle.load(input_file)
        input_file.close()
    except EOFError:
        contacts_dict = {}
    return contacts_dict
 

def get_menu_choice():
    print('Меню')
    print('-' * 15)
    print('1. Найти контактное лицо')
    print('2. Добавить контактное лицо')
    print('3. Изменить контактное лицо')
    print('4. Удалить контактное лицо')
    print('5. Выйти из программы')
    print()
    choice = int(input('Введите выбранный пункт: '))
    while choice < LOOK_UP or choice > QUIT:
        choice = int(input('Введите выбранный пункт: '))
    return choice


def look_up(mycontacts):
    name = input('Введите имя: ')
    print(mycontacts.get(name, 'Имя не найдено'))
    
    
def add(mycontacts):
    name = input('Имя: ')
    phone = input('Телефон: ')
    email = input('Электронный адрес: ')
    entry = contact.Contact(name, phone, email)
    if name not in mycontacts:
        mycontacts[name] = entry
        print('Запись добавлена')
    else:
        print('Это имя уже существует')
    
    
def change(mycontacts):
    name = input('Введите имя: ')
    if name in mycontacts:
        phone = input('Введите новый телефонный номер: ')
        email = input('Введите новый электронный адрес: ')
        entry = contact.Contact(name, phone, email)
        mycontacts[name] = entry
        print('Информация обновлена')
    else:
        print('Это имя не найдено')
            
            
def delete(mycontacts):
    name = input('Введите имя: ')
    if name in mycontacts:
        del mycontacts[name]
        print('Запись удалена')
    else:
        print('Это имя не найдено')
            
            
def save_contacts(mycontacts):
    outfile = open(FILENAME, 'wb')
    pickle.dump(mycontacts, outfile)
    outfile.close()
    
if __name__ == '__main__':
    main()