import json
from typing import Dict, Any


def save_data_json(data: Any, filename: str = "data.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


def load_data_json(filename: str = "data.json"):
    with open(filename, "r") as f:
        return json.load(f)


def add_data_json(new_data: Dict[str, Any], filename: str = "data.json"):
    try:
        old_data = load_data_json(filename)
        if not isinstance(old_data, list):
            old_data = [old_data]  # If data is dict, transform in to the list
    except FileNotFoundError:
        old_data = []  # If file not found, create a new list
    old_data.append(new_data)  # Add new dict to list
    print(old_data)
    save_data_json(old_data, filename)


data1 = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "skills": ["Python", "Machine Learning", "Data Analysis"],
}

data2 = {
    "name": "Alice",
    "age": 25,
    "city": "Los Angeles",
    "skills": ["JavaScript", "React", "Node.js"],
}

save_data_json([data1])  # save data to list of dictionary

add_data_json(data2)  # add new dictionary
