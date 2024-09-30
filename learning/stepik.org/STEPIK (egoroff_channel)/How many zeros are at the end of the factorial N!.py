import math


def factorial(n: int):
    return math.factorial(n)


def trailing_zeros(n: int) -> int:
    string = str(factorial(n))
    count = 0
    for i in string[::-1]:
        if i == '0':
            count += 1
        else:
            break
    return count


print(trailing_zeros(20))
