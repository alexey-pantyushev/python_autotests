import requests
import pytest


URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'e94fc8205537bbb596f4fc2aac8b7abc'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = '33617'


def test_status_code():
    respons = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert respons.status_code == 200
