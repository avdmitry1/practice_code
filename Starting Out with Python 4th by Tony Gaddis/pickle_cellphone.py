import pickle
import cellphone

FILENAME = 'cellphones.dat'
def main():
    again = 'yes'
    output_file = open(FILENAME, 'wb')
    while again == 'yes':
        man = input('Введите производителя: ')
        mod = input('Введите номер модели: ')
        retail = float(input('Введите розничную цену: '))
        phone = cellphone.CellPhone(man, mod, retail)
        pickle.dump(phone, output_file)
        again = input('Введите yes если хотите продолжить: ')
    output_file.close()
    print(f'Данные записаны в {FILENAME}')
    
if __name__ == '__main__':
    main()