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
print(player1.get_contact())
print(player1.send_message('You have transferred to PSG club'))
print('------------------------------------------------------------------------------------')
player2 = UpdateContact('Ramos', 'Sergio', 37, '+38-067-555-55-55', 'sergio@PSG.com', 'Footballer')
print(player2.get_contact())
print(player2.send_message('You have transferred to Sevilla club'))
print('------------------------------------------------------------------------------------')
print(player1.__dict__, 'obj __dict__ method')
print()
print(Contact.__dict__, 'class __dict__ method')
print('------------------------------------------------------------------------------------')
print(UpdateContact.__bases__, '--------> __base__')
print()
print(UpdateContact.__dict__, '---------> __dict__ method')
print('------------------------------------------------------------------------------------')
