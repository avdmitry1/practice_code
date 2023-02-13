def home_insurance(pay):
    return pay * 0.8


print('-' * 30)
home_value = int(input('Put your home value: '))

print(f'The minimum amount of home insurance {home_insurance(home_value)}')
print('-' * 30)
