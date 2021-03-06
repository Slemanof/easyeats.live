import requests
import json
import mysql.connector
import unidecode
import insertionMysql
import err_handling
import menu_checker

with open('api.json') as creds:
    credentials = json.load(creds)

zomato_api = credentials['zomato']


def get_location_details(query):
    headers = {
        'Accept': 'application/json',
        'user-key': zomato_api,
    }
    params = (
        ('query', query),
    )

    response = requests.get(
        'https://developers.zomato.com/api/v2.1/locations', headers=headers, params=params)
    data = response.json()

    for loc in data['location_suggestions']:
        loc_id = loc['entity_id']
        loc_type = loc['entity_type']

    loc_info = []
    loc_info.append(loc_id)
    loc_info.append(loc_type)
    return loc_info


def get_restaurants(ent_id, ent_type, start):
    headers = {
        'Accept': 'application/json',
        'user-key': zomato_api,
    }

    params = (
        ('entity_id', ent_id),
        ('entity_type', ent_type),
    )

    link = 'https://developers.zomato.com/api/v2.1/search?entity_id=90561&entity_type=zone&start=' + \
           str(start)

    response = requests.get(
        link, headers=headers, params=params)

    return response.json()


def get_menu(restaurant_id):
    headers = {
        'Accept': 'application/json',
        'user-key': zomato_api,
    }
    url = 'https://developers.zomato.com/api/v2.1/dailymenu?res_id='

    url1 = url + restaurant_id
    response = requests.get(url1, headers=headers)

    data = response.json()

    data = str(data).replace('\'', '\"').replace("\\xa0", " ")
    data = unidecode.unidecode(data)
    try:
        data = menu_checker.menu_checker(data)
    except json.decoder.JSONDecodeError:
        err_handling.restaurant_error(restaurant_id, 'menu')
        return '{"No daily menu at the moment":" "}'
    return data


def get_quaters():
    quaters = []
    for quater in range(1, 11):
        quaters.append(get_location_details("Praha " + str(quater)))
    return quaters


if __name__ == '__main__':
    print("Restaurants in Prague ")

for quater in get_quaters():
    x = 0
    while x < 100:
        data = get_restaurants(quater[0], quater[1], x)
        x += 20

        print(data)

        for restaurant in data['restaurants']:
            vegan = 0
            vegetarian = 0
            card_payment = 0
            gluten_free = 0
            takeaway = 0
            r = restaurant['restaurant']
            res_id = (r['R']['res_id'])
            print(res_id)
            print(r['name'].upper())
            loc = r['location']
            print(loc['address'])
            coordinates = (loc['latitude'], loc['longitude'])
            rating = r['user_rating']
            print(rating['aggregate_rating'])
            print(r['price_range'])
            print(r['cuisines'])
            print(r['featured_image'])
            print(r['highlights'])
            print(r['phone_numbers'])
            print(r['timings'])
            if 'Vegetarian Fiendly' in (r["highlights"]):
                vegetarian = 1

            if 'Vegan Options' in (r["highlights"]):
                vegan = 1
            if 'Credit Card' in (r["highlights"]):
                card_payment = 1
            if 'Gluten Free Options' in (r["highlights"]):
                gluten_free = 1
            if 'Takeaway Available' in (r["highlights"]):
                takeaway = 1

            phones = r['phone_numbers'].split(", ")


            def save_phones():
                phones_list = ['0', '0']

                if len(phones) == 0:
                    return phones_list
                elif len(phones) == 1:
                    phones_list[0] = phones[0]
                    return phones_list
                else:
                    phones_list[0] = phones[0]
                    phones_list[1] = phones[1]
                    return phones_list


            print(get_menu(str(res_id)))
            try:
                insertionMysql.insert(res_id, (r['name'].upper()), loc['address'], coordinates[0], coordinates[1],
                                      rating['aggregate_rating'], r['price_range'], r['cuisines'],
                                      r['featured_image'], vegan, vegetarian, card_payment, gluten_free, takeaway,
                                      save_phones()[0], save_phones()[1], r['timings'], str(get_menu(str(res_id))),
                                      r['menu_url'])
            except mysql.connector.errors.IntegrityError:
                continue
            except:
                err_handling.restaurant_error(res_id)
                continue
            print()
