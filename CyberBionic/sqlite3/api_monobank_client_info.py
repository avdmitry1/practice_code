import requests

API_KEY = ""
account_id = ""


def get_data_client(API_KEY, account_id):
    url = f"https://api.monobank.ua/personal/client-info"

    headers = {"X-Token": API_KEY}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None


print(get_data_client(API_KEY, account_id))
