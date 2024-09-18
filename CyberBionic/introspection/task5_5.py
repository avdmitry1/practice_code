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

    def get_contact(self): #method of the superclass (the parent class of the class in which this method is defined).
        return super().get_contact(), f'{self.job}' 


    def get_message(self, message: str):
        return f'Message: {message}'


print('------------------------------------------------------------------------------------')
player1 = Contact('Ramos', 'Sergio', 36, '+38-067-555-55-55', 'sergio@RealMadrid.com')
player2 = UpdateContact('Ramos', 'Sergio', 37, '+38-067-555-55-55', 'sergio@PSG.com', 'Footballer')
print('------------------------------------------------------------------------------------')
delattr(player2, 'job')
try:
    print(player2.get_contact())
except AttributeError:
    print('Attribute Job was deleted')
print('------------------------------------------------------------------------------------')
def get_new_contact(self):
    return super(UpdateContact, self).get_contact(), 'Attribute job was deleted, new method rewrite'
setattr(player2, 'get_contact', get_new_contact.__get__(player2, UpdateContact))
print('------------------------------------------------------------------------------------')
print(player2.get_contact())