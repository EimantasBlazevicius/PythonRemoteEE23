months_dict = {"January": 31,
               "February": "28/29",
               "March": 31,
               "April": 30,
               "May": 31,
               "June": 30,
               "July": 31,
               "August": 31,
               "September": 30,
               "October": 31,
               "November": 30,
               "December": 31
               }

user_month = input("What is the month name you want to know the amount of days to: ")
print(f"The amount of days for {user_month} is {months_dict[user_month]}")
