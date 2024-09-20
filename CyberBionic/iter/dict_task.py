products = {
    "Електроніка": ["Телефон", "Ноутбук", "Навушники"],
    "Одяг": ["Футболка", "Джинси", "Куртка"],
    "Книги": ["Роман", "Фентезі", "Наукова література"]
}

class MyIterator:
    def __init__(self, dictionary):
        self.items = list(dictionary.items())
        self.index = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < len(self.items):
            result = self.items[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

for key, values in MyIterator(products):
    for value in values:
        print((key, value))
