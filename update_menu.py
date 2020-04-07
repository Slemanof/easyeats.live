import mysql.connector
from zomato_api import get_menu


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
