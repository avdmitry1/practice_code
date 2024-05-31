def is_prime(number):
    count = 0
    for i in range(1, number + 1):
        if number % i == 0:
            count += 1
        else:
            count += 0
    return True if count == 2 else False


number = int(input())

print(f'{is_prime(number)}')
