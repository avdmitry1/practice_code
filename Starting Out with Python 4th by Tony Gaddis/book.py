class Book:
    def __init__(self, name, author, publisher):
        self.__name = name
        self.__author = author
        self.__publisher = publisher
    def set_name(self, name):
        self.__name = name
    def set_author(self, author):
        self.__author = author
    def set_publisher(self, publisher):
        self.__publisher = publisher
    def get_name(self):
        return self.__name
    def get_author(self):
        return self.__author
    def get_publisher(self):
        return self.__publisher
    def __str__(self) -> str:
        return f'Название книги -> {self.__name}\n' + \
        f'Автор -> {self.__author}\n' + \
        f'Выпущена издателем -> {self.__publisher}'
    