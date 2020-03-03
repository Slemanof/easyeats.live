import re
from bs4 import BeautifulSoup
import urllib.request

response = urllib.request.urlopen(
    'https://www.yelp.cz/search?find_desc=&find_loc=Praha%201%2C%20Praha%202').read()
soup = BeautifulSoup(response, 'html.parser')
restaurant_names_html = soup.find_all(
    class_='lemon--a__373c0__IEZFH link__373c0__1G70M link-color--inherit__373c0__3dzpk link-size--inherit__373c0__1VFlE')
restaurant_addresses_html = soup.find_all(
    class_="lemon--span__373c0__3997G raw__373c0__3rcx7")
restaurant_rating_html = soup.find_all(
    class_='lemon--span__373c0__3997G text__373c0__2Kxyz priceRange__373c0__2DY87 text-color--black-extra-light__373c0__2OyzO text-align--left__373c0__2XGa- text-bullet--after__373c0__3fS1Z')
restaurants_type_html = soup.find_all(
    class_="lemon--li__373c0__1r9wz border-color--default__373c0__3-ifU")
restaurant_type_list = []
for restaurant_type in restaurants_type_html:
    restaurant_type_list += [[restaurant_type[10:-4] for restaurant_type in re.findall(r'target="">.*?</a>', str(restaurant_type.find_all(
        class_='lemon--a__373c0__IEZFH link__373c0__1G70M link-color--inherit__373c0__3dzpk link-size--default__373c0__7tls6')))]]
restaurant_name = re.findall(r"name=\".*?\"", str(restaurant_names_html))
restaurant_star = re.findall(r'\d\.?\d? hvězdičkové hodnocení', str(soup))
restaurant_address = re.findall(r'3rcx7">.*?<', str(restaurant_addresses_html))
restaurant_address = restaurant_address[1:]
restaurant_price = re.findall(
    r'3fS1Z">.*?</span>', str(restaurant_rating_html))

for possition in range(len(restaurant_star)):
    print(restaurant_address[possition][7:-1] + " " + restaurant_name[possition][6:-1] + " " + (restaurant_star[possition])[
          :-22] + " " + restaurant_price[possition][7:-7] + " " + str(restaurant_type_list[possition]))
