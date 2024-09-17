def get_name_age(name: str, age: int) -> str:
    return f'My name is {name} and i am {age} years old'

name = input('Enter your name: ')
age = int(input('Enter your age: '))

print(get_name_age(name, age))