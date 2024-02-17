from datetime import datetime

# Morning, Day, Evening or Night.
current_hour = datetime.now().hour

if current_hour < 5:
    print("Night")
elif current_hour < 10:
    print("Morning")
elif current_hour < 18:
    print("Day")
elif current_hour < 22:
    print("Evening")
elif current_hour < 24:
    print("Night")
