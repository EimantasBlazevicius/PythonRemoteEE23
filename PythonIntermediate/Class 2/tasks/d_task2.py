import time


def log_time(func):
    # a decorator that only calls a decorated function during the day
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(end - start)

    return wrapper


@log_time
def printer():
    time.sleep(1)
    print("Some sasdasdasd")


printer()
