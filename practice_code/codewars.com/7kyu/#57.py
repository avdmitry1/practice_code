def high_and_low(numbers):
    a = [int(i) for i in numbers.split()]
    return f'{max(a)} {min(a)}'


print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))
