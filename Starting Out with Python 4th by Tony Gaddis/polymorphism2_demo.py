import animals

def main():
    mammal = animals.Mammal('Обычное животное')
    dog = animals.Dog()
    cat = animals.Cat()
    
    print('Вот несколько животных и звуки которые они издают.')
    print('-' * 30)
    show_mammal_info(mammal)
    print()
    show_mammal_info(dog)
    print()
    show_mammal_info(cat)   
    print()
    show_mammal_info('Я - последовательность символов')

def show_mammal_info(creature):
    if isinstance(creature, animals.Mammal):
        creature.show_species()
        creature.make_sound()
    else:
        print('Это не млекопитающие')
        
        
if __name__ == '__main__':
    main()