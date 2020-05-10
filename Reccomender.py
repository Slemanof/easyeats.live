

def get_recommendations(customerID, dblink, amount=3):
    # return a list of three restaurant IDs
    mycursor = dblink
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
    # count each cuisine in a dictionary
    likedCuisinesCount = {}
    for x in range(len(likedCuisines)):
        for y in range(len(likedCuisines[x])):
            if likedCuisines[x][y][0] in likedCuisinesCount:
                likedCuisinesCount[likedCuisines[x][y][0]] = likedCuisinesCount[likedCuisines[x][y][0]] + 1
            else:
                likedCuisinesCount[likedCuisines[x][y][0]] = 1
    # sort the cuisines
    cuisinesSorted = []
    for x in likedCuisinesCount:
        for y in range(amount):
            try:
                if likedCuisinesCount[x] > likedCuisinesCount[cuisinesSorted[y]]:
                    cuisinesSorted.insert(y,  x)
                    break
                elif y == len(cuisinesSorted):
                    cuisinesSorted.append(x)
                    break
            except Exception:
                cuisinesSorted.append(x)
                break
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

    cuisinesFinalSorted = []
    for x in cuisinesFinal2:
        for y in range(amount):
            try:
                if cuisinesFinal2[x] > cuisinesFinal2[cuisinesFinalSorted[y]]:
                    cuisinesFinalSorted.insert(y,  x)
                    break
                elif y == len(cuisinesFinalSorted):
                    cuisinesFinalSorted.append(x)
                    break
            except Exception:
                cuisinesFinalSorted.append(x)
                break
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

    return cuisinesFinalSorted[0:amount]


def getCustomerLiked(customerID):
    # return a list of restaurant ids that the customer liked from SQL database
    # place holder for now
    customerID = customerID
    customerLiked = [2, 1, 3, ]
    return customerLiked
