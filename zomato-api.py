import requests
import geopy.distance

zomato_api = '6bc71cad65004dd66dbb46d16667630a'


user_coordinates = []

def get_location_details(query):

    headers = {
        'Accept': 'application/json',
        'user-key': zomato_api,
    }
    params = (
        ('query', query),
    )

    response = requests.get('https://developers.zomato.com/api/v2.1/locations', headers=headers, params=params)
    data = response.json()

    for loc in data['location_suggestions']:
        loc_id = loc['entity_id']
        loc_type = loc['entity_type']

        actual_latitude = loc['latitude']
        actual_longitude = loc['longitude']

    user_coordinates.append(actual_latitude)
    user_coordinates.append(actual_longitude)


    return loc_id, loc_type





def get_restaurants(ent_id, ent_type):

    headers = {
        'Accept': 'application/json',
        'user-key': zomato_api,
    }

    params = (
        ('entity_id', ent_id),
        ('entity_type', ent_type),
    )

    response = requests.get('https://developers.zomato.com/api/v2.1/search?entity_id=90581&entity_type=zone&q=Daily%20Menu&start=30&count=50', headers=headers, params=params)

    return response.json()





def get_menu(restaurant_id):
    headers = {
        'Accept': 'application/json',
        'user-key': zomato_api,
    }
    url = 'https://developers.zomato.com/api/v2.1/dailymenu?res_id='

    url1 = url + restaurant_id
    response = requests.get(url1, headers=headers)
    print(response.json())





if __name__ == '__main__':

    prompt = '> '
    print('Enter location to search')
    q = input(prompt)
    print()

    entity_id, entity_type = get_location_details(q)
    data = get_restaurants(entity_id, entity_type)

    print("Restaurants in " + q.title() + " --\n")

    print(data)

    for restaurant in data['restaurants']:
        r = restaurant['restaurant']
        res_id = (r['R']['res_id'])
        print(res_id)
        print(r['name'].upper())
        loc = r['location']
        print(loc['address'])
        coordinates = (loc['latitude'], loc['longitude'])
        rating = r['user_rating']
        print(rating['aggregate_rating'])
        print(r['average_cost_for_two'])
        print(r['cuisines'])
        print(r['featured_image'])
        print(r['highlights'])
        print(r['phone_numbers'])
        print(str(geopy.distance.geodesic(coordinates, tuple(user_coordinates)).km)+'km')
        get_menu(str(res_id))
        print()

