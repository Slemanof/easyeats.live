import requests
import json

with open('api.json') as creds:
    credentials = json.load(creds)

google_api = credentials['google']


def get_coordinates(address):
    url1 = "https://maps.googleapis.com/maps/api/geocode/json?address="
    for word in address.split():
        url1 += word + "+"
    url1 += ",+Praha,+Czech+Republic"
    tailers = {
        "key": google_api,
    }
    re = requests.get(url1, tailers)
    data = re.json()
    latitude = ((((data['results'])[0])['geometry'])['location'])['lat']
    longitude = ((((data['results'])[0])['geometry'])['location'])['lng']
    return latitude, longitude
