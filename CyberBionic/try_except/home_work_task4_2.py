def add(x: int, y: int):
    return x + y 
    
def devide(x: int, y: int):
    try:
        return x / y
    except ZeroDivisionError:
        print(f'Cannot divide by zero')
    
def multi(x: int, y: int):
    return x * y

def subtraction(x: int, y: int):
    return x - y

def exponent(x: int, y: int):
    try:
        return x ** y
    except ZeroDivisionError:
        print(f'0 cannot be raised to a negative power')

while True:
    print('*' * 50)
    print('1 -> add')
    print('2 -> devide')
    print('3 -> multi')
    print('4 -> subtraction')
    print('5 -> exponent')
    print('exit')
    print('*' * 50)
    ask = input('What calculation would you like to do? ')
    
    if ask == 'exit'.strip().lower():
        break
    elif ask == 'add':
        x = int(input('Enter first number: '))
        y = int(input('Enter second number: '))
        print(add(x, y))
    
    elif ask == 'devide':
        x = int(input('Enter first number: '))
        y = int(input('Enter second number: '))
        print(devide(x, y))

    elif ask == 'multi':
        x = int(input('Enter first number: '))
        y = int(input('Enter second number: '))
        print(multi(x, y))

    elif ask == 'subtraction':
        x = int(input('Enter first number: '))
        y = int(input('Enter second number: '))
        print(subtraction(x, y))

    elif ask == 'exponent':
        x = int(input('Enter first number: '))
        y = int(input('Enter second number: '))
        print(exponent(x, y))
