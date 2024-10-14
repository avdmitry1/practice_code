import requests


def http_client(url: str, type_request: str, data: dict = None):
    if type_request.upper() == "GET":
        return requests.get(url, params=data)
    elif type_request.upper() == "POST":
        return requests.post(url, json=data)
    else:
        return "Invalid request type. Please choose either 'GET' or 'POST'."


def display_response(response):
    print("-----------------------")
    print(f"Status code: {response.status_code}")
    for key, value in response.headers.items():
        print(f"{key}: {value}")
    print("-----------------------")
    print(response.text)


def main():

    while True:
        print("-----------------------")
        print("Choose an option:")
        print('1. Type request "GET"')
        print('2. Type request "POST"')
        print("3. Exit")
        print("-----------------------")

        choice = input("Enter your choice: ")

        if choice == "1":
            url = input("Enter the URL: ")
            try:
                data = http_client(url, "GET")
                display_response(data)
            except Exception as e:
                print(f"An error occurred: {e}")

        elif choice == "2":
            url = input("Enter the URL: ")
            try:
                data = http_client(
                    url, "POST", {"title": "foo", "body": "bar", "userId": 1}
                )
                display_response(data)
            except Exception as e:
                print(f"An error occurred: {e}")

        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")


#  'https://jsonplaceholder.typicode.com/posts'

if __name__ == "__main__":
    main()
