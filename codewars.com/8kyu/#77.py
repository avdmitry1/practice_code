def hello(name=''):
    name = name.lower()
    return f'Hello, {name.title() or "World"}!'


print(hello('aLIce'))
