import re
import csv
from bs4 import BeautifulSoup
import urllib.request

response = urllib.request.urlopen(
    'https://www.yelp.cz/search?find_desc=&find_loc=Praha%201%2C%20Praha%202&start=30').read()
soup = BeautifulSoup(response, 'html.parser')
restaurants__html = soup.find_all(
    class_='lemon--div__373c0__1mboc largerScrollablePhotos__373c0__3FEIJ arrange__373c0__2C9bH border-color--default__373c0__3-ifU')
restaurant_type_pattern = r"lemon--a__373c0__IEZFH link__373c0__1G70M link-color--inherit__373c0__3dzpk link-size--default__373c0__7tls6\" href=\".*?\" rel=\"\" role=\".*?\">.*?<"
restaurant_name_link_pattern = r"lemon--a__373c0__IEZFH link__373c0__1G70M link-color--inherit__373c0__3dzpk link-size--inherit__373c0__1VFlE\" href=\".*?\" name=\".*?\""
restaurant_price_pattern = r"\"lemon--span__373c0__3997G text__373c0__2Kxyz priceRange__373c0__2DY87 text-color--black-extra-light__373c0__2OyzO text-align--left__373c0__2XGa- text-bullet--after__373c0__3fS1Z\">.*?<"
restaurant_name_pattern = r'name=\".*?\"'
restaurant_price_pattern = r"\"lemon--span__373c0__3997G text__373c0__2Kxyz priceRange__373c0__2DY87 text-color--black-extra-light__373c0__2OyzO text-align--left__373c0__2XGa- text-bullet--after__373c0__3fS1Z\">.*?<"
restaurant_address_pattern = r"emon--span__373c0__3997G raw__373c0__3rcx7\">.*?<"
# A path should be modified according to your file location
with open('/home/Basurman/restaurant_recommender_2001/restaurant_dataset_yelp.csv', mode='w') as csv_file:
    fieldnames = ['rest_name', 'rest_star', 'vegetarian', 'price', 'address']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for restaurant in restaurants__html:
        if(['target="">Památky<'] in [re.findall(r"target=\"\">.*?<", name) for name in ((re.findall(restaurant_type_pattern, str(restaurant))))]):
            continue
        else:
            veg = False
            if (['target="">Vegetariánská kuchyně<'] in [re.findall(r"target=\"\">.*?<", name) for name in ((re.findall(restaurant_type_pattern, str(restaurant))))]):
                veg = True
            name_link = re.findall(
                restaurant_name_link_pattern, str(restaurant))[0]
            writer.writerow(
                {'rest_name': (((re.findall(restaurant_name_pattern, name_link))[0])[6:-1]).replace("&amp;", "&"), 'rest_star': ((re.findall(r'\d\.?\d? hvězdičkové hodnocení', str(restaurant)))[0])[:-22], 'vegetarian': veg, 'price': ((re.findall(restaurant_price_pattern, str(restaurant)))[0])[180:-1], 'address': ((re.findall(restaurant_address_pattern, str(restaurant)))[0])[44:-1]})