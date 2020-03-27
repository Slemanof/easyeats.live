import mysql.connector


def insert(res_id, res_name, res_address, res_rating, res_cost, res_cuisine):
    cnx = mysql.connector.connect(user='script', password='LetMeIn:)123',
                                  host='127.0.0.1',
                                  database='restaurant_recommender')
    cursor = cnx.cursor()
    add_restaurant = ("INSERT INTO restaurant (id, name, address, rating, cost_for_2) VALUES (" +
                      str(res_id) + ", \""+res_name+"\", \""+res_address+"\", \""+str(res_rating)+"\", \""+str(res_cost)+"\")")
    cursor.execute(add_restaurant)
    cnx.commit()
    return


# insert(4, 'Test4', "Na pankraci", 4.5, 400 , "Czech")


def check_cuisines(cuisine):
    cnx = mysql.connector.connect(user='script', password='LetMeIn:)123',
                                  host='127.0.0.1',
                                  database='restaurant_recommender')
    cursor = cnx.cursor()
    try:
        add_cuisine = ("SELECT id FROM cuisines WHERE name = " + cuisine)
        cursor.execute(add_cuisine)
        return
    except mysql.connector.errors.ProgrammingError:
        cursor.execute(
            "INSERT INTO cuisines (name) VALUES (\"" + cuisine+"\")")
    except mysql.connector.errors.IntegrityError:
        return
    cnx.commit()
    return


# check_cuisines("Bulgar")


def cuisines(res_id, res_cuisine):
    cuisines_list = res_cuisine.split(",")
    cnx = mysql.connector.connect(user='script', password='LetMeIn:)123',
                                  host='127.0.0.1',
                                  database='restaurant_recommender')
    cursor = cnx.cursor()
    for cuisine in cuisines_list:
        check_cuisines(cuisine)
        add_restaurant_cuisine =("INSERT INTO restaurant_cuisine (restaurant_id, cuisine_id) VALUES ("+res_id+",(SELECT id FROM cuisines WHERE name = \""+res_cuisine+"\"))")
        cursor.execute(add_restaurant_cuisine)
        cnx.commit()
    return