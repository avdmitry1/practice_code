import pickle

def main():
    again = 'd'
    output_file = open('info.dat', 'wb')
    while again.lower() == 'd':
        save_data(output_file)
        again = input('Повторить ввод данных? d/n ')
    output_file.close
    
def save_data(file):
    person = {}
    person['Имя'] = input('Имя: ')
    person['Возраст'] = int(input('Возраст: '))
    person['Масса'] = float(input('Масса: '))
    
    pickle.dump(person, file)
    
if __name__ == '__main__':
    main()