import requests 

api_key = 'c8c33b48-afa7-4bb2-bc56-b91cd3919b56'
word = 'Potato'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

res = requests.get(url)

definitions = res.json()

for definition in definitions:
    print(definition)