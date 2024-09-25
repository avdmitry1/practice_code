import json

products = [
    {
        "id": 1,
        "name": "Laptop",
        "category": "Electronics",
        "price": 1200.99,
        "stock": 15,
        "description": "15-inch laptop with 16GB RAM and 512GB SSD.",
    },
    {
        "id": 2,
        "name": "Smartphone",
        "category": "Electronics",
        "price": 799.99,
        "stock": 30,
        "description": "Latest model with 128GB storage and 5G support.",
    },
    {
        "id": 3,
        "name": "Headphones",
        "category": "Accessories",
        "price": 199.99,
        "stock": 50,
        "description": "Noise-cancelling wireless headphones with 20-hour battery life.",
    },
    {
        "id": 4,
        "name": "Coffee Maker",
        "category": "Home Appliances",
        "price": 89.99,
        "stock": 20,
        "description": "Automatic coffee maker with built-in grinder.",
    },
    {
        "id": 5,
        "name": "Backpack",
        "category": "Accessories",
        "price": 49.99,
        "stock": 100,
        "description": "Water-resistant backpack with multiple compartments.",
    },
]


with open("products.json", "w") as file:
    """create products.json file"""
    json.dump(products, file, indent=4)

    
with open("products.json", "r") as file:
    """load products from products.json file"""
    json_data = json.load(file)
    


print(json_data)
