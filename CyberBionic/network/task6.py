import requests


def get_request():
    url = "https://jsonplaceholder.typicode.com/comments"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        for comment in data[0:20]:
            print(
                f'Id: {comment["id"]}, Name: {comment["name"]}, Email: {comment["email"]}, Body: {comment["body"]}'
            )
    else:
        print(f"Error: {response.status_code}")


def post_request():
    url = "https://jsonplaceholder.typicode.com/comments"
    payload = {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "body": "This is a sample comment.",
    }
    response = requests.post(url, json=payload)
    if response.status_code == 201:
        print(f"Comment created successfully. ID: {response.json()['id']}")
    else:
        print(f"Error: {response.status_code}")


def put_request():
    url = "https://jsonplaceholder.typicode.com/comments/1"
    payload = {
        "name": "Jane Doe",
        "email": "jane.doe@example.com",
        "body": "This is an updated comment.",
    }
    response = requests.put(url, json=payload)
    if response.status_code == 200:
        print("Comment updated successfully.")
    else:
        print(f"Error: {response.status_code}")

def delete_request():
    url = "https://jsonplaceholder.typicode.com/comments/1"
    response = requests.delete(url)
    if response.status_code == 200:
        print("Comment deleted successfully.")
    else:
        print(f"Error: {response.status_code}")


# get_request()
# post_request()
# put_request()
# delete_request()