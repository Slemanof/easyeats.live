def choose_delivery():
    n = 0
    while n < 1:
        global delivery_option
        delivery_option = input("Choose your delivery option (delivery / no delivery): ")
        if delivery_option == "delivery":
            n = n + 1
            break
        elif delivery_option == "no delivery":
            n = n + 1
            break
        else:
            print("Your input is invalid, please pay attention to the capitalzation and try again!")
            continue
    print("You have selected the option: " + delivery_option)
# ---------------------------------------------------------------------------------------------------------


def choose_cuisine():
    available_cuisines = ["korean", "indian", "mexican"]
    n = 0
    for cuisine in available_cuisines:
        print(cuisine)
    while n < 1:
        global cuisine_option
        cuisine_option = input("Choose your cuisine option from the above list: ")
        if cuisine_option in available_cuisines:
            n = n + 1
            break
        else:
            print("Your input is invalid, please pay attention to the capitalzation and try again!")
            continue
    print("You have selected the option: " + cuisine_option)
# ---------------------------------------------------------------------------------------------------------


def choose_price():
    price_categories = ["cheap", "moderate", "expensive"]
    n = 0
    for price in price_categories:
        print(price)
    while n < 1:
        global price_option
        price_option = input("Please select your price option from the above list: ")
        if price_option == "cheap":
            n = n + 1
            break
        elif price_option == "moderate":
            n = n + 1
            break
        elif price_option == "expensive":
            n = n + 1
            break
        else:
            print("Your input is invalid, please pay attention to the capitalzation and try again!")
            continue
    print("You have selected the option: " + price_option)


# ---------------------------------------------------------------------------------------------------------

def summarize():
    print("HERE IS A SUMMARY OF YOUR SELECTION:")
    print(delivery_option)
    print(cuisine_option)
    print(price_option)


# ---------------------------------------------------------------------------------------------------------


choose_delivery()
choose_cuisine()
choose_price()
summarize()
