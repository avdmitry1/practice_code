import class_pet

def main():
    name = input('Введите название животного: ')
    animal_type = input('Введите тип животного: ')
    age = input('Введите возраст животного: ')
    pet = class_pet.Pet(name, animal_type, age)
    print(pet)
if __name__ == '__main__':
    main()