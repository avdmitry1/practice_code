import vehicles

def main():
    used_car = vehicles.Car('Audi', 2007, 12500, 21500.0, 4)
    print('Изготовитель -', used_car.get_make(), 'Motors')
    print('Модель -', used_car.get_model(), 'Year')
    print('Пробег -', used_car.get_mileage(), 'Miles')
    print('Цена -', used_car.get_price(), '$')
    print('Количество дверей -', used_car.get_doors())
    
if __name__ == '__main__':
    main()