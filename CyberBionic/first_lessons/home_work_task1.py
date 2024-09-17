def get_name(name: str) -> str:
    return f'Welcome to CyberBionic course {name}!'

user_name = input('Enter your name: ')
print(get_name(user_name))