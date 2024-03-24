from datetime import datetime


# Concept of passing one function as an argument to another function
def write_text():
    print("Hello World")


def main(func):
    func()


# main(write_text)


# Concept of creating function inside of another function
def func1():
    def internal_function():
        pass

    return internal_function


# Simple decorator
def disable_at_night(func):
    # a decorator that only calls a decorated function during the day
    def wrapper():
        if 9 <= datetime.now().hour < 22:
            func()

    return wrapper


# Decorator with proterties
def run_only_between(from_=7, to_=22):
    # a decorator that only calls a decorated function at certain times
    def dec(func):
        def wrapper():
            if from_ <= datetime.now().hour < to_:
                func()

        return wrapper

    return dec


# Usage of decorator

@disable_at_night
def say_something():
    print("Hello room wrapped function")


@run_only_between(10, 21)
def say_something1():
    print("Hello world wrapped function")


@run_only_between(9, 21)
def say_something2():
    print("Hello room wrapped function")


say_something()
say_something1()
say_something2()
