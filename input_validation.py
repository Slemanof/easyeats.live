def menu_checker(menu):
    if menu == '{"daily_menus": [], "status": "success"}' or menu == '{"code": 400, "status": "Bad Request", "message": "No Daily Menu Available"}':
        return '\"No daily menu at the moment\"'
    else:
        return menu
