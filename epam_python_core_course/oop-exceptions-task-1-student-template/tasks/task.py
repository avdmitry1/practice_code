class Pagination:
    def __init__(self, data: str, items_on_page: int):
        self.data = data
        self.items_on_page = items_on_page

    def page_count(self):
        return len(self.data)
    
    def item_count(self):
        return len

    def count_items_on_page(self, page_number):
        pass

    def find_page(self, data):
        pass
    
    def display_page(self, page_number):
        return self.data.split()[page_number]
    
