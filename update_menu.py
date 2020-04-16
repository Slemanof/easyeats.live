import mysql.connector
import requests
import unidecode
import json

with open('api.json') as creds:
    credentials = json.load(creds)

zomato_api = credentials['zomato']

def get_menu(restaurant_id):
    headers = {
        'Accept': 'application/json',
        'user-key': zomato_api,
    }
    url = 'https://developers.zomato.com/api/v2.1/dailymenu?res_id='

    url1 = url + restaurant_id
    response = requests.get(url1, headers=headers)

    data = response.json()

    data = str(data).replace('\'', '\"')
    data = unidecode.unidecode(data)
    return data


def update_menu_database(res_id, menu):
    cnx = mysql.connector.connect(user='script', password='LetMeIn:)123',
                                  host='127.0.0.1',
                                  database='restaurant_recommender')
    cursor = cnx.cursor()
    update_sql = ("UPDATE restaurant SET  menu =\'" +
                  menu + "\'  WHERE id = "+str(res_id))
    cursor.execute(update_sql)
    cnx.commit()
    cursor.close()
    cnx.close()


def update_main():
    cnx = mysql.connector.connect(user='script', password='LetMeIn:)123',
                                  host='127.0.0.1',
                                  database='restaurant_recommender')
    cursor = cnx.cursor()
    get_ids = ("SELECT id FROM restaurant")
    cursor.execute(get_ids)
    for row in cursor:
        update_menu_database((row[0]), (get_menu(str(row[0]))))
    cursor.close()
    cnx.close()


update_main()
