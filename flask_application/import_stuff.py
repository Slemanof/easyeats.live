import json


def get_keys():
    with open('api.json') as creds:
        credentials = json.load(creds)
    key = credentials['encryption_key']
    return key
