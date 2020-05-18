import json
import pytest
import menu_checker as mc


# using test_menu1 as input checks if output is correct for status: success & empty menu
test_menu_1 = '{"daily_menus": [], "status": "success"}'
# using test_menu2 as input checks if output is correct for: (code: 400 status: Bad Request)
test_menu_2 = '{"code": 400, "status": "Bad Request", "message": "No Daily Menu Available"}'
# using test_menu3 as input checks if output is correct for a correctly filled out menu
test_menu_3 = '{"status": "success", "daily_menus": [{"daily_menu": {"name": "Takeaway", "dishes": [{"dish": {"name": "Cheesecake", "price": "200 CZK", "dish_id": "1"}},{"dish": {"name": "Chocolate cake", "price": "500 CZK", "dish_id": "2"}}, {"dish": {"name": "Schwarzwald cake", "price": "350 CZK", "dish_id": "3"}}]}}]}'


def test_menu_checker():
    # Checking expected outputs
    assert mc.menu_checker(
        test_menu_1) == '{"No daily menu at the moment": " "}', "Incorrect Output"
    assert mc.menu_checker(
        test_menu_2) == '{"No daily menu at the moment": " "}', "Incorrect Output"
    # Checking output of dummy json
    assert mc.menu_checker(
        test_menu_3) == '{"Cheesecake": "200 CZK", "Chocolate cake": "500 CZK", "Schwarzwald cake": "350 CZK"}', "Incorrect Output"
    #


test_menu_checker()
