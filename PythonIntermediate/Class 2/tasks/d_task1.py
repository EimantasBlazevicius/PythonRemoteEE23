import time
from datetime import datetime


def log_time(func):
    # a decorator that only calls a decorated function during the day
    def wrapper():
        print(datetime.today().time())
        func()
        print(datetime.today().time())

    return wrapper


@log_time
def printer():
    time.sleep(1)
    print("Some sasdasdasd")


printer()
