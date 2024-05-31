import random


def even_odd(counter):
    even = 0
    odd = 0
    for i in counter:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd


random_numbers = [random.randint(1, 100) for i in range(101)]
result = even_odd(random_numbers)

print(f'EVEN = {result[0]}, ODD = {result[1]}')
