def ticket_price():
    A = int(input('Number of class A tickets sold -> '))
    B = int(input('Number of class B tickets sold -> '))
    C = int(input('Number of class C tickets sold -> '))
    return A * 20, B * 15, C * 10


price_a, price_b, price_c = ticket_price()
print(
    f'The amount of income from ticket sales was ${price_a + price_b + price_c}'
)
