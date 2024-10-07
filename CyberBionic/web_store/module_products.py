
import json

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

    def add_product(
        self,
        product_id: int,
        name: str,
        category: str,
        price: float,
        product_count: int,
        description: str,
    ) -> "Product":
        """Add a new product and print a success message."""
        new_product = Product(product_id, name, category, price, product_count, description)
        print(f"Product {new_product.name} added successfully.")
        return new_product

    def update_product_count(self, new_product_count: int):
        """Update the product count."""
        if new_product_count <= 0:
            raise ValueError("Product count must be greater than 0.")
        self.product_count = new_product_count

    def change_product_count(self, value: int):
        """Change the product count by a given value."""
        new_product_count = self.product_count + value
        if new_product_count < 0:
            raise ValueError("Product count cannot be negative.")
        self.product_count = new_product_count

    def update_price(self, value: float):
        """Update the price."""
        if value <= 0:
            raise ValueError("Price must be greater than 0.")
        self.price = value

    def __str__(self) -> str:
        return (
            f"Product ID: {self.product_id}\n"
            f"Name: {self.name}\n"
            f"Category: {self.category}\n"
            f"Price: ${self.price:.2f}\n"
            f"Product Count: {self.product_count}\n"
            f"Description: {self.description}"
        )

    def to_json(self) -> str:
        """Convert the product instance to a JSON string."""
        return json.dumps(self.__dict__, indent=2)

    @classmethod
    def from_json(cls, json_string: str) -> "Product":
        """Create a Product instance from a JSON string."""
        data = json.loads(json_string)
        return cls(**data)

    def save_to_file(self, filename: str):
        """Save the product instance to a file in JSON format."""
        with open(filename, 'w') as f:
            json.dump(self.__dict__, f, indent=2)

    @classmethod
    def load_from_file(cls, filename: str) -> "Product":
        """Load a Product instance from a file in JSON format."""
        with open(filename, 'r') as f:
            data = json.load(f)
        return cls(**data)
    

# Example usage
product = Product(1, "Lenovo", "Laptop", 450.0, 100, "Lenovo IDEA Pad gaming 3")
# print(product)

# Add another product
new_product = product.add_product(2, 'Samsung', 'Mobile', 300.0, 200, 'Samsung Galaxy S20 Ultra')
# print(new_product)

# Convert to JSON
json_str = product.to_json()
print(json_str)

# Save to file
product.save_to_file('product.json')

# Load from file
loaded_product = Product.load_from_file('product.json')
print(loaded_product)




