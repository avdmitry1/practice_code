def main():
    num1 = int(input('Введите значение 1 '))
    num2 = int(input('Введите значение 2 '))

    quotient = divide(num1, num2)

    if quotient is None:
        print('Деление на ноль невозможно')
    else:
        print(f'{num1} поделить на {num2} равняется {quotient}')


def divide(num1, num2):
    if num2 == 0:
        result = None
    else:
        result = num1 / num2
    return result


main()
