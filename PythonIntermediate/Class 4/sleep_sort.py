import threading
from time import sleep

numbers_to_sort = [4, 2, 6, 9, 3]

sorted = []
threads = []


def sort_func(num):
    sleep(0.1 * num)
    sorted.append(num)


for number in numbers_to_sort:
    thread = threading.Thread(target=sort_func, args=(number,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print(sorted)
