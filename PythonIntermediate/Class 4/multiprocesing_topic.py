import multiprocessing as mp
import time

result_a = []
result_b = []
result_c = []


def do_math(numbers):
    for number in numbers:
        result_a.append(number ** 3)


def do_math_two(numbers):
    for number in numbers:
        result_b.append(number ** 5)


def do_math_three(numbers):
    for number in numbers:
        result_c.append(number ** 3)


list_numbers = list(range(9000000))
mp_one = mp.Process(target=do_math, args=(list_numbers,))
mp_two = mp.Process(target=do_math_two, args=(list_numbers,))
mp_three = mp.Process(target=do_math_three, args=(list_numbers,))

if __name__ == "__main__":
    start1 = time.perf_counter()
    mp_one.start()
    mp_two.start()
    mp_three.start()
    end1 = time.perf_counter()
    print(end1 - start1)

    start2 = time.perf_counter()
    do_math(list_numbers)
    do_math_two(list_numbers)
    do_math_three(list_numbers)
    end2 = time.perf_counter()
    print(end2 - start2)
