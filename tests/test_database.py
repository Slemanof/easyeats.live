import mysql.connector


def test_db():
    cnx = mysql.connector.connect(user='script', password='LetMeIn:)123',
                                  host='127.0.0.1',
                                  database='restaurant_recommender')

    assert True == cnx.is_connected()
    cnx.close()
