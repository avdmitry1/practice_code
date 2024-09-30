def estate_tax():
    print('-' * 30)
    estate_value = int(input('What is the value of real estate? '))
    return estate_value * 0.60


print(f'Estate tax is {estate_tax()}')
print('-' * 30)
