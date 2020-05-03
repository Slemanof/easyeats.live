import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="restaurants"
)

mycursor = mydb.cursor()


def get_recommendations(customerID):
    # return a list of three restaurant IDs
    customerID = customerID
    someID = getCustomerLiked(customerID)
    likedList = []
    for x in range(len(someID)):
        sql = "SELECT id, vegan, vegetarian, credit_card, gluten_free, takeaway FROM restaurant WHERE id = %s"
        testID = (someID[x],)
        mycursor.execute(sql, testID)
        likedList.append(mycursor.fetchone())

    likedCuisines = []
    for x in range(len(someID)):
        sql = "SELECT cuisine_id FROM restaurant_cuisine WHERE restaurant_id = %s"
        testID = (someID[x],)
        mycursor.execute(sql, testID)
        likedCuisines.append(mycursor.fetchall())

    likedCuisinesCount = {}
    for x in range(len(likedCuisines)):
        for y in range(len(likedCuisines[x])):
            if likedCuisines[x][y][0] in likedCuisinesCount:
                likedCuisinesCount[likedCuisines[x][y][0]] = likedCuisinesCount[likedCuisines[x][y][0]] + 1
            else:
                likedCuisinesCount[likedCuisines[x][y][0]] = 1

    cuisinesSorted = [0, 0, 0]

    for x in likedCuisinesCount:
        if likedCuisinesCount[x] > cuisinesSorted[0]:
            cuisinesSorted[2] = cuisinesSorted[1]
            cuisinesSorted[1] = cuisinesSorted[0]
            cuisinesSorted[0] = x
        elif likedCuisinesCount[x] > cuisinesSorted[1]:
            cuisinesSorted[2] = cuisinesSorted[1]
            cuisinesSorted[1] = x
        elif likedCuisinesCount[x] > cuisinesSorted[2]:
            cuisinesSorted[2] = x

    cuisinesFinal = []
    for x in range(len(cuisinesSorted)):
        sql = "SELECT restaurant_id FROM restaurant_cuisine WHERE cuisine_id = %s"
        cuisine_id = (cuisinesSorted[x],)
        mycursor.execute(sql, cuisine_id)
        cuisinesFinal.append(mycursor.fetchall())
    cuisinesFinal2 = {}

    for x in range(len(cuisinesFinal)):
        for y in range(len(cuisinesFinal[x])):
            if cuisinesFinal[x][y][0] in cuisinesFinal2:
                cuisinesFinal2[cuisinesFinal[x][y][0]] = cuisinesFinal2[cuisinesFinal[x][y][0]] + 1
            else:
                cuisinesFinal2[cuisinesFinal[x][y][0]] = 1

    cuisinesFinalSorted = [0, 0, 0]

    for x in cuisinesFinal2:
        if cuisinesFinal2[x] > cuisinesFinalSorted[0]:
            cuisinesFinalSorted[2] = cuisinesFinalSorted[1]
            cuisinesFinalSorted[1] = cuisinesFinalSorted[0]
            cuisinesFinalSorted[0] = x
        elif cuisinesFinal2[x] > cuisinesFinalSorted[1]:
            cuisinesFinalSorted[2] = cuisinesFinalSorted[1]
            cuisinesFinalSorted[1] = x
        elif cuisinesFinal2[x] > cuisinesFinalSorted[2]:
            cuisinesFinalSorted[2] = x

    vegan = 0
    vegetarian = 0
    credit_card = 0
    gluten_free = 0
    takeaway = 0

    for x in range(len(likedList)):
        if likedList[x][1]:
            vegan = vegan + 1
        if likedList[x][2]:
            vegetarian = vegetarian + 1
        if likedList[x][3]:
            credit_card = credit_card + 1
        if likedList[x][4]:
            gluten_free = gluten_free + 1
        if likedList[x][5]:
            takeaway = takeaway + 1

    return cuisinesFinalSorted


def getCustomerLiked(customerID):
    # return a list of restaurant ids that the customer liked from SQL database
    # place holder for now
    customerID = customerID
    customerLiked = [2, 1, 3, ]
    return customerLiked
