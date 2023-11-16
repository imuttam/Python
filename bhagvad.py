import requests

BASE_URL = 'https://bhagavadgitaapi.in/'

response = requests.get(f'{BASE_URL}/get-chapters.html', headers={"Content-Type":"application/json"})

# print(response.status_code)
json_data = response.json()

print(json_data)
