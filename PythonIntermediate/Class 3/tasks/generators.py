import random


def gen_even(number):
    start = 0
    while start <= number:
        if start % 2 == 0:
            yield start


def gen_infinite(start, step):
    the_number = start
    while True:
        yield the_number
        the_number += step


def gen_random_with_edges(start, end):
    for _ in range(10):
        yield random.randint(start, end)


def gen_to_zero(start):
    the_number = start
    while the_number != 0:
        yield the_number
        the_number -= 1


def gen_large_file():
    with open('test.csv', 'r') as f:
        while True:
            line = f.readline()
            if line != '':
                yield f.readline().strip()


for item in gen_large_file():
    print(item)
