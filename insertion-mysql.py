import mysql.connector


def check_cuisines(cuisine):
    cuisine_exisits = False
    cnx = mysql.connector.connect(user='script', password='LetMeIn:)123',
                                  host='127.0.0.1',
                                  database='restaurant_recommender')
    cursor = cnx.cursor()
    add_cuisine = ("SELECT id FROM cuisines WHERE name = \"" + cuisine + "\"")
    cursor.execute(add_cuisine)
    for row in cursor:
        if type(row[0]) == int:
            cuisine_exisits = True
            return
    if cuisine_exisits == False:
        cursor.execute("INSERT INTO cuisines (name) VALUES (\"" + cuisine+"\")")
    cnx.commit()
    cursor.close()
    cnx.close()
    return


check_cuisines("Czech")


def cuisines(res_id, res_cuisine):
    cuisines_list = res_cuisine.split(",")
    cnx = mysql.connector.connect(user='script', password='LetMeIn:)123',
                                  host='127.0.0.1',
                                  database='restaurant_recommender')
    cursor = cnx.cursor()
    for cuisine in cuisines_list:
        check_cuisines(cuisine)
        add_restaurant_cuisine = ("INSERT INTO restaurant_cuisine (restaurant_id, cuisine_id) VALUES ("+str(
            res_id)+",(SELECT id FROM cuisines WHERE name = \""+cuisine+"\"))")
        cursor.execute(add_restaurant_cuisine)
    cnx.commit()
    cursor.close()
    cnx.close()
    return

# cuisines(1, "Czech")

def insert(res_id, res_name, res_address, res_rating, res_cost, res_cuisine):
    cnx = mysql.connector.connect(user='script', password='LetMeIn:)123',
                                  host='127.0.0.1',
                                  database='restaurant_recommender')
    cursor = cnx.cursor()
    add_restaurant = ("INSERT INTO restaurant (id, name, address, rating, cost_for_2) VALUES (" +
                      str(res_id) + ", \""+res_name+"\", \""+res_address+"\", \""+str(res_rating)+"\", \""+str(res_cost)+"\")")
    cursor.execute(add_restaurant)
    cnx.commit()
    cursor.close()
    cnx.close()
    cuisines(res_id, res_cuisine)
    return

insert(6, 'Test6', "Na pankraci", 4.5, 400 , "Czech, Bulgar")