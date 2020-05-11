import mysql.connector

def get_res_coord():
    cnx = mysql.connector.connect(user='admin', password='Didistar12',
                                host='127.0.0.1',
                                database='restaurant_recommender')
    cursor = cnx.cursor()
    get_restaurants = ("SELECT latitute, longitude FROM restaurant")
    cursor.execute(get_restaurants)
    restaurant_coords = []
    for row in cursor:
        restaurant_coords.append(row)
    cursor.close()
    return restaurant_coords

for restaurant in get_res_coord():
    print(restaurant)
