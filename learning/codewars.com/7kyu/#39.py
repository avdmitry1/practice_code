import math


def factorial(n):
    if n < 0 or n > 12:
        raise ValueError

    return math.factorial(n)
    # multi = 1
    # for i in range(1, n + 1):
    #     multi *= i
    # return multi


print(factorial(40))
