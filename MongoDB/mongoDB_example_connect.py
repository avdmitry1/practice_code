"""
Example of connecting to MongoDB and inserting data using PyMongo.

This script connects to a MongoDB Atlas cluster, creates a database named "test",
and a collection named "customers". It then inserts three documents into the
collection.

The CONNECTION_STRING variable must be replaced with a valid connection string
to a MongoDB Atlas cluster.
"""

from pymongo import MongoClient


CONNECTION_STRING = "mongodb+srv://user_name:password@test.7402i.mongodb.net/"


def connect_to_mongo(connection_string: str) -> MongoClient:
    """
    Connect to a MongoDB cluster.

    Args:
        connection_string (str): The connection string to the MongoDB cluster.

    Returns:
        MongoClient: The MongoClient object or None if the connection failed.
    """
    try:
        client = MongoClient(connection_string)
        client.server_info()
        return client
    except Exception as error:
        print(f"Error connecting to MongoDB: {error}")
        return None


def main():
    """
    Main function to connect to MongoDB and insert data.
    """
    client = connect_to_mongo(CONNECTION_STRING)
    if client:
        database = client["test"]
        customers_collection = database["customers"]
        customer_documents = [
            {"name": "Alice", "age": 30, "city": "New York"},
            {"name": "Bob", "age": 25, "city": "Los Angeles"},
            {"name": "Charlie", "age": 35, "city": "Chicago"},
        ]
        try:
            insert_result = customers_collection.insert_many(customer_documents)
            print("Data inserted successfully:", insert_result.inserted_ids)
        except Exception as error:
            print(f"Error inserting data: {error}")


if __name__ == "__main__":
    main()
