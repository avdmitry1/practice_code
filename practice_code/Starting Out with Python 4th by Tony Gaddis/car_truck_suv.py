import vehicles

def main():
    car = vehicles.Car('BMW', 2001, 70000, 15000.0, 4)
    truck = vehicles.Truck('Toyota', 2002, 40000, 12000.0, '4WD')
    suv = vehicles.SUV('Volvo', 2000, 30000, 18500.0, 5)
    print('ПОДДЕРЖАНЫЕ АВТО НА СКЛАДЕ')
    print('-' * 20)
    print('Изготовитель -', car.get_make())
    print('Модель -', car.get_model(), 'Year')
    print('Пробег -', car.get_mileage(), 'Miles')
    print('Цена -', car.get_price(), '$')
    print('Количество дверей -', car.get_doors())
    print('-----ПИКАП-----')
    print('Изготовитель -', truck.get_make())
    print('Модель -', truck.get_model(), 'Year')
    print('Пробег -', truck.get_mileage(), 'Miles')
    print('Цена -', truck.get_price(), '$')
    print('Тип привода', truck.get_drive_type())
    print('-----SUV-----')
    print('Изготовитель -', suv.get_make())
    print('Модель -', suv.get_model(), 'Year')
    print('Пробег -', suv.get_mileage(), 'Miles')
    print('Цена -', suv.get_price(), '$')
    print('Количество мест', suv.get_pass_cap())
    
if __name__ == '__main__':
    main()