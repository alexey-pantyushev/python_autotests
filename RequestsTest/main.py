import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'e94fc8205537bbb596f4fc2aac8b7abc'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}
body_create = {
    "name": "generate",
    "photo_id": -1
}

body_change_name = {
    "pokemon_id": "334525",
    "name": "Barabulka",
    "photo_id": -1
}

body_catch_pokeomon = {
    "pokemon_id": "334525"
}



'''respons_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(respons_create.text)'''

'''respons_change_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change_name)
print(respons_change_name.text)'''

respons_catch_pokeomon = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch_pokeomon)
print(respons_catch_pokeomon.text)


