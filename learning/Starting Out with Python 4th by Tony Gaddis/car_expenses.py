def car_expenses():
    print('-' * 30)
    loan_payment = int(input('What is your loan payment? '))
    insurance = int(input('What is the cost of insurance? '))
    gasoline = int(input('What are the costs of gasoline? '))
    engine_oil = int(input('What is the cost of engine oil? '))
    tires = int(input('What is the price of tires? '))
    maintenance = int(input('What is the cost of maintenance? '))
    return loan_payment + insurance + gasoline + engine_oil + tires + maintenance


month = car_expenses()
year = month * 12
print('-' * 30)
print(f'Monthly cost of car expenses is {month}')
print(f'The annual cost of the car is {year}')
print('-' * 30)
