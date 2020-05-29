import requests
import json

with open('api.json') as creds:
    credentials = json.load(creds)

zomato_api = credentials['zomato']


def test_api():
    headers = {
        'Accept': 'application/json',
        'user-key': zomato_api,
    }
    url = 'https://developers.zomato.com/api/v2.1/'

    response = requests.get(url, headers=headers)
    assert response.status_code == 200
