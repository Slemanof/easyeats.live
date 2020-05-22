import json

from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = ''
app.config['MYSQL_USER'] = ''
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = ''

mysql = MySQL(app)

@app.route('/home', methods=['GET', 'POST'])
def home():
    current_user = 1
    cur = mysql.connection.cursor()
    chosen_filters = request.args.to_dict(flat=False)

    cuisines_option_query = cuisines_option(chosen_filters)

    location_option_query = location_option(cuisines_option_query, chosen_filters)

    cur.execute(additional_options(location_option_query, chosen_filters))
    data = cur.fetchall()

    new_data = []
    for i in data:
        new_data.append(list(i))

    for i in new_data:
        i[6] = json.loads(i[6])
        i[15] = json.loads(i[15])

   like_list = check_liked_restaurants(current_user, cursor)

    if request.method == "POST":
        like_and_unlike(current_user, cursor)

    return render_template('index.html', data=new_data, like_list=like_list)


def additional_options(query, filters):
    additional_filters = ['vegetarian', 'vegan', 'gluten_free', 'credit_card', 'takeaway']
    for filter_name in additional_filters:
        if filter_name in filters:
            query = "SELECT * FROM (%s) as t WHERE %s=1 " % (query, filter_name)
        else:
            query = "SELECT * FROM (%s) as t" % query

    return query


def cuisines_option(filters):
    query_fragment = """SELECT r.id, r.name, r.address, r.image, r.rating, r.price_range, r.timing,
                        r.vegan, r.vegetarian, r.gluten_free, r.credit_card, r.takeaway,
                        r.phone_num1, r.phone_num2, r.usual_menu_url, r.menu,
                        r.latitute, r.longitude, GROUP_CONCAT(c.name separator ', ') as cuisines
                        FROM restaurant r LEFT JOIN
                        restaurant_cuisine rc
                        ON rc.restaurant_id = r.id LEFT JOIN
                        cuisines c
                        ON c.id = rc.cuisine_id"""

    if 'cuisines' in filters:
        cuisines = tuple(filters.get('cuisines'))

        if len(cuisines) == 1:
            filtered_by_cuisine = ("%s WHERE c.name = '%s' GROUP BY r.id " % (query_fragment, cuisines[0]))

        else:
            filtered_by_cuisine = ("%s WHERE c.name in %s GROUP BY r.id " % (query_fragment, cuisines))

    else:
        filtered_by_cuisine = ("%s GROUP BY r.id " % query_fragment)

    return filtered_by_cuisine


def location_option(cuisine_query, filters):
    query_fragment = """id, name, address, image, rating, price_range, timing,
                vegan, vegetarian, gluten_free, credit_card, takeaway,
                phone_num1, phone_num2, usual_menu_url, menu, latitute,
                longitude"""

    if 'lat' and 'lon' in filters:

        lat = filters.get('lat')[0]
        lon = filters.get('lon')[0]

        formula = ("""(6371 * acos(cos( radians(%s
                )) * cos( radians( latitute )) * cos( radians( longitude ) - radians(%s
                ) ) + sin( radians(%s
                ) ) * sin( radians( latitute ))))""" % (lat, lon, lat))

        filtered_by_distance = ("""SELECT %s, cuisines,
                   FORMAT(%s, 2) AS distance,
                   FORMAT((%s * 12), 1) AS time
                   FROM (%s) as t HAVING distance < 3 ORDER
                   BY distance""" % (query_fragment, formula, formula, cuisine_query))

    else:
        filtered_by_distance = ("SELECT * FROM (%s) as t" % cuisine_query)

    return filtered_by_distance


def check_liked_restaurants(user_id, cur):
    liked_restaurants = []
    check_user_query = """SELECT EXISTS(SELECT user_id FROM restaurant_user WHERE user_id = %s)""" % user_id
    cur.execute(check_user_query)
    check_user_result = cur.fetchone()

    if check_user_result[0] == 0:
        return liked_restaurants
    else:
        liked_restaurants_query = """SELECT restaurant_id FROM restaurant_user WHERE user_id = %s""" % user_id
        cur.execute(liked_restaurants_query)
        liked_restaurants_result = cur.fetchall()
        for rest_id in liked_restaurants_result:
            liked_restaurants.append(rest_id[0])
        return liked_restaurants

    
def like_and_unlike(user_id, cur):
    rest_id = request.json.get('restId', None)
    print(rest_id)

    check_if_liked_query = "SELECT EXISTS(SELECT * FROM restaurant_user WHERE user_id = %s AND restaurant_id = %s ) " \
                           % (user_id, rest_id)

    cur.execute(check_if_liked_query)
    check_result = cur.fetchone()
    if check_result[0] == 0:
        query = "INSERT INTO restaurant_user (restaurant_id, user_id) VALUES (%s, %s)" % (rest_id, user_id)

    else:
        query = "DELETE FROM restaurant_user WHERE restaurant_id = %s AND user_id = %s " % (rest_id, user_id)

    cur.execute(query)
    mysql.connection.commit()



if __name__ == "__main__":
    app.run()
