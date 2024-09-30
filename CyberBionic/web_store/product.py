class Product:
    def __init__(
        self,
        product_id: int,
        name: str,
        category: str,
        price: float,
        product_count: int,
        description: str,
    ):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.product_count = product_count
        self.description = description

    def update_product_count(self, new_product_count: int):
        """update the product count"""
        if new_product_count <= 0:
            raise ValueError("Product count is 0.")
        self.product_count = new_product_count

    def changing_product_count(self, value: int):
        """change the product count"""
        new_product_count = self.product_count + value
        if new_product_count < 0:
            print("Products count is 0")
        self.product_count = new_product_count

    def update_price(self, value: int):
        """update the price"""
        if value <= 0:
            raise ValueError("Price cannot be 0 or negative.")
        self.price = value

    def __str__(self) -> str:
        return f"Product ID: {self.product_id}\nName: {self.name}\nCategory: {self.category}\nPrice: ${self.price}\nProduct Count: {self.product_count}\nDescription: {self.description}"
