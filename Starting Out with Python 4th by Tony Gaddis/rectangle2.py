# Площадь треугольника
def area(width, length):
    return width * length

# Периметр треугольника


def perimeter(width, length):
    return 2 * (width + length)

# Функция мейн для тестирования


def main():
    width = float(input('Put width: '))
    length = float(input('Put length: '))
    print(f'Area equal {area(width, length)}')
    print(f'Perimeter equal {perimeter(width, length)}')


if __name__ == '__main__':
    main()
