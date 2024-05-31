def get_miles(km):
    miles = km * 0.6214
    return miles


print('-' * 30)
kilometer = int(input('Введите количество километров: '))
print(f'{kilometer} км будет равно -> {get_miles(kilometer):,.2f} миль')
print('-' * 30)
