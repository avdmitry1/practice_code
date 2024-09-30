import math


def main():
    a = float(input('Введите длину стороны А: '))
    b = float(input('Введите длину стороны Б: '))

    c = math.hypot(a, b)

    print(f'Длина гипотенузы составляет {c}')


main()
