from lxml import etree

data = etree.parse("libraries.xml")


def find_books_by_genre(genre):
    books = data.xpath(
        f'//book[genre="{genre}"]'
    )  # Searches for all <book> elements in which the <genre>
    # element has the text "Programming".
    for book in books:
        title = book.find("title").text
        author = book.find("author").text
        year = book.find("year").text
        print(f"Title: {title}, Author: {author}, Year: {year}")


find_books_by_genre("Programming")
