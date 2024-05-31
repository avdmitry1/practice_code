class PriceControl:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError("Price must be between 0 and 100.")
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        raise AttributeError("Cannot delete the price attribute")

class NameControl:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if self.name in instance.__dict__:
            raise ValueError(f"{self.name.capitalize()} can not be changed.")
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        raise AttributeError(f"Cannot delete the {self.name} attribute")

class Book:
    price = PriceControl('price')
    author = NameControl('author')
    name = NameControl('name')

    def __init__(self, author, name, price):
        self.author = author
        self.name = name
        self.price = price

# Example usage
b = Book("William Faulkner", "The Sound and the Fury", 12)
print(f"Author='{b.author}', Name='{b.name}', Price='{b.price}'")
