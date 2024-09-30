import Circle
import Rectangle

AREA_CIRCLE_CHOICE = 1
CIRCUMFERENCE_CHOICE = 2
AREA_RECTANGE_CHOICE = 3
PERIMETER_RECTANGLE_CHOICE = 4
QUIT_CHOICE = 5


def main():
    choice = 0

    while choice != QUIT_CHOICE:
        # Показать меню
        display_menu()
        # Получить вариант выбора пользователя
        choice = int(input('Введите вариант: '))
        # Выполнить выбранное действие
        if choice == AREA_CIRCLE_CHOICE:
            radius = float(input('Введите радиус круга: '))
            print('Площадь равна', Circle.area(radius))

        elif choice == CIRCUMFERENCE_CHOICE:
            radius = float(input('Введите радиус круга: '))
            print('Длинна окружности равна', Circle.circumference(radius))

        elif choice == AREA_RECTANGE_CHOICE:
            width = float(input('Введите ширину прямоугольника: '))
            length = float(input('Введите длину прямоугольника: '))
            print('Площадь равна', Rectangle.area(width, length))

        elif choice == PERIMETER_RECTANGLE_CHOICE:
            width = float(input('Введите ширину прямоугольника: '))
            length = float(input('Введите длину прямоугольника: '))
            print('Периметр равен', Rectangle.perimeter(width, length))

        elif choice == QUIT_CHOICE:
            print('Выходим из программы')
        else:
            print('Ошибка, недопустимый выбор')

# Функция дисплей показывает меню


def display_menu():
    print('MENU')
    print('1. Площадь круга')
    print('2. Длина окружности')
    print('3. Площадь прямоугольника')
    print('4. Периметр прямиоугольника')
    print('5. Выход')


main()
