from datetime import datetime


def what_time(hour):
    if hour < 5:
        return "Night"
    elif hour < 10:
        return "Morning"
    elif hour < 18:
        return "Day"
    elif hour < 22:
        return "Evening"
    elif hour < 24:
        return "Night"


# Morning, Day, Evening or Night.
current_hour = datetime.now().hour
print(what_time(current_hour))
