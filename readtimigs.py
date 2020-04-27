import re


def findtime(time):
    if re.match(r'Closed', time):
        return 'Closed'
    result = ''
    for time in re.findall(r"\d{2}:\d{2}", time):
        result += time + "-"
    return result[:-1]


week_dict = {"Mon": 0, "Tue": 1, "Wed": 2,
             "Thu": 3, "Fri": 4, "Sat": 5, "Sun": 6}
week_lst = ["Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday", "Sunday"]


def put_timings_order(row, days, hrs_dict):
    days = days.replace(")", "")
    for day in days.split(", "):
        hrs_dict[week_lst[week_dict[day]]] = findtime(row)
    return hrs_dict


def put_timings_interval(row, days, hrs_dict):
    days = days.replace(")", "")
    start = week_dict[days.split("-")[0]]
    stop = week_dict[days.split("-")[1]]
    time = findtime(row)
    for day in range(start, stop+1):
        hrs_dict[week_lst[day]] = time
    return hrs_dict


def put_timings_standalone(row, day, hrs_dict):
    hrs_dict[week_lst[week_dict[day]]] = findtime(row)
    return hrs_dict


def get_opening_hrs(zomato_timing):
    opening_hrs_dict = {}
    for row in zomato_timing.split("),"):
        order_days = re.findall(r"[D-Z][a-z]{2}, [D-Z][a-z]{2}", row)
        interval_days = re.findall(
            r"[D-Z][a-z]{2}-[D-Z][a-z]{2}", row)
        standalone_days = re.findall(r"[D-Z][a-z]{2}", row)
        if order_days:
            opening_hrs_dict = put_timings_order(
                row, order_days[0], opening_hrs_dict)
        if interval_days:
            opening_hrs_dict = put_timings_interval(
                row, interval_days[0], opening_hrs_dict)
        if standalone_days:
            opening_hrs_dict = put_timings_standalone(
                row, standalone_days[0], opening_hrs_dict)
    return str(opening_hrs_dict)
