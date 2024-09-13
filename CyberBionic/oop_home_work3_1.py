class Car:


    def __init__(self, brand: str, model: str, price: float, color: str) -> None:
        self.brand = brand
        self.model = model
        self.__price = price
        self.color = color
    

    def set_price(self, new_price: int) -> None:
        print(f'Welcome to our dealer center!')
        asking = input('Do you have customer card? yes/no: ').strip().lower()
        if not asking.isalpha():
            asking = input('Invalid enter! please use yes/no: ').strip().lower()
        elif asking == 'yes':
            self.__price *= (1 - new_price / 100)


    def get_price(self) -> float:
        return self.__price


    def __str__(self) -> str:
        return f'Brand -> {self.brand}, \nModel -> {self.model}, \nColor -> {self.color}.'


client1 = Car('Audi', 'A5', 55000.00, 'white')
client1.set_price(5)
print('*' * 55)
print(f'Your new price for this car is {client1.get_price()}$')
print(client1)
print('*' * 55)