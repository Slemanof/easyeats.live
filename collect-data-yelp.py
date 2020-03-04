import re
import csv
from bs4 import BeautifulSoup
import urllib.request

response = urllib.request.urlopen(
    'https://www.yelp.cz/search?find_desc=&find_loc=Praha%201%2C%20Praha%202&start=20').read()
soup = BeautifulSoup(response, 'html.parser')
restaurants__html = soup.find_all(
    class_='lemon--div__373c0__1mboc largerScrollablePhotos__373c0__3FEIJ arrange__373c0__2C9bH border-color--default__373c0__3-ifU')
restaurant_type_pattern = r"lemon--a__373c0__IEZFH link__373c0__1G70M link-color--inherit__373c0__3dzpk link-size--default__373c0__7tls6\" href=\".*?\" rel=\"\" role=\".*?\">.*?<"
print(re.findall(restaurant_type_pattern, str(restaurants__html[2])))
i = 0
for restaurant in restaurants__html:
    if(['target="">Památky<'] in [re.findall(r"target=\"\">.*?<", name) for name in ((re.findall(restaurant_type_pattern, str(restaurant))))]):
        continue
    else:
        i += 1
        print(i)
