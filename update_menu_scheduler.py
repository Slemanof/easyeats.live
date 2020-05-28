from datetime import datetime
from threading import Timer
import update_menu


def update_menu_scheduled():
    x = datetime.today()
    y = x.replace(day=x.day + 1)
    delta_t = (y-x).seconds
    update_menu.update_main()
    Timer(delta_t, update_menu_scheduled).start()


update_menu_scheduled()
