import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'a7da3fde3daa81da477dfa9837bb5400'
HEADER = {'Content-Type' : 'application/json' , 'trainer_token': TOKEN}

body_registration = {
    'trainer_token': TOKEN,
    "email": "msyradoeva@yandex.ru",
    "password": "1236495Margo"
}
body_confirmation = {"trainer_token": TOKEN
}
body_create = {
    
    "name": "generate",
    "photo_id": -1

}
body_change = {
    "pokemon_id": "234695",
    "name": "New Name",
    "photo_id": 2
}
body_pokeball = {
    "pokemon_id": "234694"
}


'''response = requests.post(url= f'{URL}/trainers/reg' , headers = HEADER, json = body_registration)
print(response.text)'''

'''response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_confirmation)
print(response_confirmation.text)'''

'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

message = response_create.json()['message']
print(message)'''

'''response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change.text)

message = response_change.json()['message']
print(message)'''

response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_change)
print(response_pokeball.text)

message = response_pokeball.json()['message']
print(message)