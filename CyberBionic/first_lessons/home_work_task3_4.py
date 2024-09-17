import math
def calculator(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    elif operator == '%':
        return num1 % num2 and num2 != 0
    elif operator == '//':
        return num1 // num2
    elif operator == 'pow':
        return num1 ** (1 / num2)
    elif operator == 'cos':
        return math.cos(num1)
    elif operator == 'sin':
        return math.sin(num1)
    elif operator == 'tan':
        return math.tan(num1)
    
print(calculator(1, 2, '+'))