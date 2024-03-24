def function_sum(x):
    return x + 5


function_sum(9)
# There are the same thing
l_sum = lambda x: x + 5

l_sum(9)

print((lambda x, y: x * y)(2, 9))

example_list = [5, 2, 3, 4, 6, 7, 8, 9]
# function filter
filter_result = list(filter(lambda x: x % 2 == 0, example_list))

print(filter_result)

# function map
map_result = list(map(lambda x: x + 2, example_list))
list_method = [x + 2 for x in example_list]

print(map_result)

# sorting
example_list_sort = [[1, 3], [3, 1], [4, 2], [2, 4]]

simple_sorted = sorted(example_list_sort)
print(simple_sorted)

smarter_sorted = sorted(example_list_sort, key=lambda x: x[1])
print(smarter_sorted)
