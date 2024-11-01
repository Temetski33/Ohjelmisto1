# Moduuli 12 teht 1

import requests

url = f"https://api.chucknorris.io/jokes/random"
response = requests.get(url)
response_body = response.json()
print(response_body['value'])