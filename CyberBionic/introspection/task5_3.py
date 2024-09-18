class Contact:
    def __init__(self, surname: str, name: str, age: int, mob_phone: str, email: str):
        self.surname = surname
        self.name = name
        self.age = age
        self.mob_phone = mob_phone
        self.email = email

    def get_contact(self):
        return f'Name: {self.name} {self.surname}, Age: {self.age}, Mob. Phone: {self.mob_phone}, Email: {self.email}'

    def send_message(self, message: str):
        return f'Sending message to {self.name}: {message}'


class UpdateContact(Contact):
    def __init__(self, surname: str, name: str, age: int, mob_phone: str, email: str, job: str):
        super().__init__(surname, name, age, mob_phone, email)
        self.job = job

    def get_message(self, message: str):
        return f'Message: {message}'


print('------------------------------------------------------------------------------------')
player1 = Contact('Ramos', 'Sergio', 36, '+38-067-555-55-55', 'sergio@RealMadrid.com')
player2 = UpdateContact('Ramos', 'Sergio', 37, '+38-067-555-55-55', 'sergio@PSG.com', 'Footballer')
print(hasattr(player1, 'name'))  #True if player has 'name' attribute
print(hasattr(player1, 'city'))  #False if not
print('------------------------------------------------------------------------------------')
try:
    print(getattr(player2, 'city'))  #Try get the 'city' attribute
except AttributeError:
    print('Object has no "city" attribute')  #Exception AttributeError
print(getattr(player2, 'city', 'Madrid'))  #Object gets new 'city' attribute with value 'Madrid'
print('------------------------------------------------------------------------------------')
setattr(player2, 'age', 38)  #Set the new value of age attribute
setattr(player2, 'city', 'Madrid')  #Object sets new 'city' attribute with value 'Madrid'
print(player2.__dict__)
print(player2.get_contact())
print(player2.city)
print('------------------------------------------------------------------------------------')
delattr(player2, 'city')  #Delete the attribute 'city' from object player2
try:
    print(player2.city)
except AttributeError:
    print('Object has no "city" attribute')
print(player2.__dict__)
print('------------------------------------------------------------------------------------')
