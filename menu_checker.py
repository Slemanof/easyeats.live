import json

def menu_checker(menu):
    if menu == '{"daily_menus": [], "status": "success"}' or menu == '{"code": 400, "status": "Bad Request", "message": "No Daily Menu Available"}':
        str_dict = {"No daily menu at the moment":" "}
        return json.dumps(str_dict)
    else:

        menu = json.loads(menu, strict=False)

        dish_dict = {}

        for dish in menu['daily_menus'][0]['daily_menu']['dishes']:
            if dish['dish']['name'] not in dish_dict:
                dish_dict[dish['dish']['name']] = dish['dish']['price']

        return json.dumps(dish_dict)


