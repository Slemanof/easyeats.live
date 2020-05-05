from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = ''
app.config['MYSQL_USER'] = ''
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = ''

mysql = MySQL(app)


@app.route('/', methods=['GET'])
def home():
    cur = mysql.connection.cursor()
    result = request.args.to_dict(flat=False)

    fields = """id, name, address, image, rating, price_range, timing,
                                            vegan, vegetarian, gluten_free, credit_card, takeaway,
                                            phone_num1, phone_num2, usual_menu_url, menu, latitute,
                                            longitude"""

    if 'cuisines' in result:
        cuisines = tuple(result.get('cuisines'))

        if len(cuisines) == 1:
            filter_by_cuisine = ("""SELECT r.id, r.name, r.address, r.image, r.rating, r.price_range, r.timing,
                                            r.vegan, r.vegetarian, r.gluten_free, r.credit_card, r.takeaway,
                                            r.phone_num1, r.phone_num2, r.usual_menu_url, r.menu, r.latitute,
                                            r.longitude, GROUP_CONCAT(c.name separator ', ') as cuisines
                                            FROM restaurant r LEFT JOIN
                                             restaurant_cuisine rc
                                             ON rc.restaurant_id = r.id LEFT JOIN
                                             cuisines c
                                             ON c.id = rc.cuisine_id
                                             WHERE c.name = '%s'
                                             GROUP BY r.id
                                            """ % cuisines[0])

        else:
            filter_by_cuisine = ("""SELECT r.id, r.name, r.address, r.image, r.rating, r.price_range, r.timing,
                                            r.vegan, r.vegetarian, r.gluten_free, r.credit_card, r.takeaway,
                                            r.phone_num1, r.phone_num2, r.usual_menu_url, r.menu, r.latitute,
                                            r.longitude, GROUP_CONCAT(c.name separator ', ') as cuisines
                                            FROM restaurant r LEFT JOIN
                                             restaurant_cuisine rc
                                             ON rc.restaurant_id = r.id LEFT JOIN
                                             cuisines c
                                             ON c.id = rc.cuisine_id
                                             WHERE c.name in %s
                                             GROUP BY r.id
                                            """ % (cuisines,))

    else:
        filter_by_cuisine = """SELECT r.id, r.name, r.address, r.image, r.rating, r.price_range, r.timing,
                                            r.vegan, r.vegetarian, r.gluten_free, r.credit_card, r.takeaway,
                                            r.phone_num1, r.phone_num2, r.usual_menu_url, r.menu, r.latitute,
                                            r.longitude, GROUP_CONCAT(c.name separator ', ') as cuisines
                                            FROM restaurant r LEFT JOIN
                                            restaurant_cuisine rc
                                            ON rc.restaurant_id = r.id LEFT JOIN
                                            cuisines c
                                            ON c.id = rc.cuisine_id
                                            GROUP BY r.id
                                                        """

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

    if 'Payment+by+card' in result:
        filter_by_payment = \
            ("""SELECT * FROM (%s) AS t WHERE credit_card = 'Payments by card accepted' """ % filter_by_distance)
    else:
        filter_by_payment = filter_by_distance

    if 'Vegan' in result:
        filter_by_vegan = ("SELECT * FROM (%s) AS t WHERE vegan = 'Vegan' " % filter_by_payment)

    else:
        filter_by_vegan = filter_by_payment

    if 'Vegetarian' in result:
        filter_by_vegetarian = ("SELECT * FROM (%s) AS t WHERE vegetarian = 'Vegetarian' " % filter_by_vegan)

    else:
        filter_by_vegetarian = filter_by_vegan

    if 'Gluten+Free' in result:
        filter_by_gf = ("SELECT * FROM (%s) AS t WHERE gluten_free = 'Gluten Free' " % filter_by_vegetarian)

    else:
        filter_by_gf = filter_by_vegetarian

    if 'Takeaway+option' in result:
        filter_by_takeaway = \
            ("SELECT * FROM (%s) AS t WHERE takeaway = 'Takeaway option available' " % filter_by_gf)

    else:
        filter_by_takeaway = filter_by_gf

    cur.execute(filter_by_takeaway)
    data = cur.fetchall()
    print(data)

    return render_template('distance.html', data=data)


if __name__ == "__main__":
    app.run(debug=True)
