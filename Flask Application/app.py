import json

from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'irina'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'restApp'

mysql = MySQL(app)


@app.route('/', methods=['GET'])
def home():
    cur = mysql.connection.cursor()
    result = request.args.to_dict(flat=False)

    fields = """id, name, address, image, rating, price_range, timing,
                                            vegan, vegetarian, gluten_free, credit_card, takeaway,
                                            phone_num1, phone_num2, usual_menu_url, menu, latitute,
                                            longitude"""

    cuisine_query = """SELECT r.id, r.name, r.address, r.image, r.rating, r.price_range, r.timing,
                                                r.vegan, r.vegetarian, r.gluten_free, r.credit_card, r.takeaway,
                                                r.phone_num1, r.phone_num2, r.usual_menu_url, r.menu,
                                                r.latitute, r.longitude, GROUP_CONCAT(c.name separator ', ') as cuisines
                                                FROM restaurant r LEFT JOIN
                                                restaurant_cuisine rc
                                                ON rc.restaurant_id = r.id LEFT JOIN
                                                cuisines c
                                                ON c.id = rc.cuisine_id"""

    if 'cuisines' in result:
        cuisines = tuple(result.get('cuisines'))

        if len(cuisines) == 1:
            filter_by_cuisine = ("%s WHERE c.name = '%s' GROUP BY r.id " % (cuisine_query, cuisines[0]))

        else:
            filter_by_cuisine = ("%s WHERE c.name = '%s' GROUP BY r.id " % (cuisine_query, (cuisines,)))

    else:
        filter_by_cuisine = ("%s GROUP BY r.id " % cuisine_query)

    if 'lat' and 'lon' in result:

        lat = result.get('lat')[0]
        lon = result.get('lon')[0]

        formula = ("""(6371 * acos(cos( radians(%s
                )) * cos( radians( latitute )) * cos( radians( longitude ) - radians(%s
                ) ) + sin( radians(%s
                ) ) * sin( radians( latitute ))))""" % (lat, lon, lat))

        filter_by_distance = ("""SELECT %s, cuisines,
                   FORMAT(%s, 2) AS distance,
                   FORMAT((%s * 12), 1) AS time
                   FROM (%s) as t HAVING distance < 3 ORDER
                   BY distance""" % (fields, formula, formula, filter_by_cuisine))

    else:
        filter_by_distance = ("SELECT * FROM (%s) as t" % filter_by_cuisine)

        def additional_options(query):
        additional_filters = ['vegetarian', 'vegan', 'gluten_free', 'credit_card', 'takeaway']
        for filter_name in additional_filters:
            if filter_name in result:
                query = "SELECT * FROM (%s) as t WHERE %s=1 " % (query, filter_name)
            else:
                query = "SELECT * FROM (%s) as t" % query

        return query

    cur.execute(additional_options(filter_by_distance))
    data = cur.fetchall()

    return render_template('index.html', data=data)


if __name__ == "__main__":
    app.run(debug=True)
