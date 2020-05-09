import sys


def restaurant_error(id, reason=False):
    if reason == False:
        err_string = str(id) + '\n'
    elif reason == 'menu':
        err_string = str(id) + " bad menu\n"

    f = open(sys.path[0] + "/zomato_api_logs.txt", "a")
    f.write(err_string)
