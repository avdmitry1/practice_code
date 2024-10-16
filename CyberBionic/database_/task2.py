import xml.etree.ElementTree as ET


data = ET.Element('libraries') # create root element

book1 = ET.SubElement(data, 'book') # create book
ET.SubElement(book1, 'title').text = 'Python Programming' # create elements
ET.SubElement(book1, 'author').text = 'John Doe'
ET.SubElement(book1, 'year').text = '2020'
ET.SubElement(book1, 'genre').text = 'Programming'

book2 = ET.SubElement(data, 'book')
ET.SubElement(book2, 'title').text = 'Learning XML'
ET.SubElement(book2, 'author').text = 'Jane Smith'
ET.SubElement(book2, 'year').text = '2018'
ET.SubElement(book2, 'genre').text = 'Programming'

book3 = ET.SubElement(data, 'book')
ET.SubElement(book3, 'title').text = 'Advanced Python'
ET.SubElement(book3, 'author').text = 'Alice Brown'
ET.SubElement(book3, 'year').text = '2022'
ET.SubElement(book3, 'genre').text = 'Programming'

tree = ET.ElementTree(data)
with open('libraries.xml', 'wb') as file:
    tree.write(file)

print('XML-file created')


