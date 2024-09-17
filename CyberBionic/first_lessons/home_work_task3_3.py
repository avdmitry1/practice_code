def quadratic_equation(a: int, b: int, c: int) -> tuple:
    D = b ** 2 - 4 * a * c
    if D < 0:
        return 'Відсутність дійсних коренів'
    elif D == 0:
        x = -b / (2 * a) 
    else:
        x1 = (-b + D ** 0.5) / (2 * a)
        x2 = (-b - D ** 0.5) / (2 * a)
    
    return x1, x2

a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
c = int(input('Enter third number: '))
print(quadratic_equation(a, b, c))