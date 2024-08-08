def sum_nums(a: int, b: int, x: int) -> str:
    return f'Result of the product numbers are - {a * b * x}'

a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
x = int(input('Enter third number: '))
print(sum_nums(a, b, x))
