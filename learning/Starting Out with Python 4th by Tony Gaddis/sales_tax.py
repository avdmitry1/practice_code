def federal_tax(sales):
    return sales * 0.05


def municipal_tax(sales):
    return sales * 0.025


def sales_tax():
    print('-' * 30)
    sales = int(input('What is the volume of sales per month: '))
    print(f'The municipal sales tax amount is ${municipal_tax(sales)}')
    print(f'The federal sales tax amount is ${federal_tax(sales)}')
    print('-' * 30)


if __name__ == '__main__':
    sales_tax()
