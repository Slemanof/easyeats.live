import sys
import os


def restaurant_error(id):
    f = open(sys.path[0] + "/zomato_api_logs.txt", "a")
    f.write(str(id) + "\n")
