

def get_recommendations(customer_id, dblink, amount=3):
    # return a list of three restaurant IDs
    mycursor = dblink
    customer_id = customer_id
    liked_restaurants = get_customer_liked(customer_id)
    liked_restaurant_details = []

    vegan = 0
    vegetarian = 0
    credit_card = 0
    gluten_free = 0
    takeaway = 0

    for x in range(len(liked_restaurant_details)):
        if liked_restaurant_details[x][1]:
            vegan = vegan + 1
        if liked_restaurant_details[x][2]:
            vegetarian = vegetarian + 1
        if liked_restaurant_details[x][3]:
            credit_card = credit_card + 1
        if liked_restaurant_details[x][4]:
            gluten_free = gluten_free + 1
        if liked_restaurant_details[x][5]:
            takeaway = takeaway + 1

    for x in range(len(liked_restaurants)):
        sql = "SELECT id, vegan, vegetarian, credit_card, gluten_free, takeaway FROM restaurant WHERE id = %s"
        test_id = (liked_restaurants[x],)
        mycursor.execute(sql, test_id)
        liked_restaurant_details.append(mycursor.fetchone())

    liked_cuisines = []
    for x in range(len(liked_restaurants)):
        sql = "SELECT cuisine_id FROM restaurant_cuisine WHERE restaurant_id = %s"
        test_id = (liked_restaurants[x],)
        mycursor.execute(sql, test_id)
        liked_cuisines.append(mycursor.fetchall())
    # count each cuisine in a dictionary
    liked_cuisines_counted = {}
    for x in range(len(liked_cuisines)):
        for y in range(len(liked_cuisines[x])):
            if liked_cuisines[x][y][0] in liked_cuisines_counted:
                liked_cuisines_counted[liked_cuisines[x][y][0]] = liked_cuisines_counted[liked_cuisines[x][y][0]] + 1
            else:
                liked_cuisines_counted[liked_cuisines[x][y][0]] = 1

    # sort the cuisines
    cuisines_sorted = []
    for x in liked_cuisines_counted:
        for y in range(len(liked_cuisines_counted)):
            try:
                if liked_cuisines_counted[x] > liked_cuisines_counted[cuisines_sorted[y]]:
                    cuisines_sorted.insert(y,  x)
                    break
                elif y == len(cuisines_sorted):
                    cuisines_sorted.append(x)
                    break
            except Exception:
                cuisines_sorted.append(x)
                break

    restaurants_recommended = []
    for x in range(len(cuisines_sorted)):
        sql = "SELECT restaurant_id FROM restaurant_cuisine WHERE cuisine_id = %s"
        cuisine_id = (cuisines_sorted[x],)
        mycursor.execute(sql, cuisine_id)
        restaurants_recommended.append(mycursor.fetchall())

    restaurants_counted = {}

    for x in range(len(restaurants_recommended)):
        for y in range(len(restaurants_recommended[x])):
            tmp = get_restaurant_details(restaurants_recommended[x][y][0], mycursor)
            if restaurants_recommended[x][y][0] in restaurants_counted:
                restaurants_counted[restaurants_recommended[x][y][0]] = restaurants_counted[restaurants_recommended[x][y][0]] + 1
                if vegan > len(liked_restaurants) * 0.8 and tmp[1]:
                    restaurants_counted[restaurants_recommended[x][y][0]] = restaurants_counted[restaurants_recommended[x][y][0]] + 1
                if vegetarian > len(liked_restaurants) * 0.8 and tmp[2]:
                    restaurants_counted[restaurants_recommended[x][y][0]] = restaurants_counted[restaurants_recommended[x][y][0]] + 1
                if credit_card > len(liked_restaurants) * 0.8 and tmp[3]:
                    restaurants_counted[restaurants_recommended[x][y][0]] = restaurants_counted[restaurants_recommended[x][y][0]] + 1
                if gluten_free > len(liked_restaurants) * 0.8 and tmp[4]:
                    restaurants_counted[restaurants_recommended[x][y][0]] = restaurants_counted[restaurants_recommended[x][y][0]] + 1
                if takeaway > len(liked_restaurants) * 0.8 and tmp[5]:
                    restaurants_counted[restaurants_recommended[x][y][0]] = restaurants_counted[restaurants_recommended[x][y][0]] + 1
            else:
                restaurants_counted[restaurants_recommended[x][y][0]] = 1

    restaurants_sorted = []
    for x in restaurants_counted:
        for y in range(amount):
            if x not in liked_restaurants:
                try:
                    if restaurants_counted[x] > restaurants_counted[restaurants_sorted[y]]:
                        restaurants_sorted.insert(y,  x)
                        break
                    elif y == len(restaurants_sorted):
                        restaurants_sorted.append(x)
                        break
                except Exception:
                    restaurants_sorted.append(x)
                    break

    return restaurants_sorted[0:amount]


def get_customer_liked(customer_id):
    # return a list of restaurant ids that the customer liked from SQL database
    # place holder for now
    customer_id = customer_id
    customer_liked = [2, 4, 3, ]
    return customer_liked


def get_restaurant_details(restaurant_id, db_link):
    mycursor = db_link
    sql = "SELECT id, vegan, vegetarian, credit_card, gluten_free, takeaway FROM restaurant WHERE id = %s"
    test_id = (restaurant_id,)
    mycursor.execute(sql, test_id)
    result = mycursor.fetchone()
    return result



