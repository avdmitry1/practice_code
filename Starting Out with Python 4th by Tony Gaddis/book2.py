import book

def main():
    name = input('Введите название книги: ')
    author = input('Введите название автора: ')
    publisher = input('Введите название издателя: ')
    the_book = book.Book(name, author, publisher)
    print(the_book)
    
if __name__ == '__main__':
    main()