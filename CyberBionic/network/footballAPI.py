import requests

api_key = 'a8bfe9d8d95541259cbd8b8e4360a339'
url = f'https://api.football-data.org/v4/matches/1'
headers = {
    'X-Auth-Token': api_key
}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    for name in data['matches']:
        print(name)
        
else:
    print(f"Error: {response.status_code}")