import requests

api_key = '42d899ca-dc47-43ec-90de-6feec4579121'
word = 'banana'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

res = requests.get(url)

definitions = res.json()

print(definitions)

for definition in definitions:
    print(definition)