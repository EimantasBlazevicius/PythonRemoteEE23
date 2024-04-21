some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # Iterable

for item in some_list:  # Iteration
    print(item)

print('-=-' * 20)

some_list2 = iter([10, 20, 30, 40, 50, 60, 70, 80, 90])  # Iterator


# print("First")
# print(next(some_list2))
# print(next(some_list2))
# print(next(some_list2))
# print(next(some_list2))


# while True:
#     try:
#         print(next(some_list2))
#     except StopIteration:
#         print("Done")
#         break


# Generator
def generator(some_number=0):
    some_text = "bla bla bla"
    for _ in range(50):
        some_number += 1
        yield f'{some_text} - {some_number}'
        print('Yield Done its job')


random_generator = (i * 2 for i in [1, 2, 23, 6, 5, 4, 8, 5])

for item in generator(9):
    print(item)
