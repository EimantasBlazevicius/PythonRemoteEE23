# list_var = []
# dictionary_var = {'key': 'value'}
# tuple_var = ()
# set_var = {'value', 'value', 'value'}

# Tuple -> Immutable data structure
magic_list = ("dog", "cat", 2000, 5, True)

print(magic_list.count('dog'))
print(magic_list.index("dog"))
print(magic_list[2])

# Set
# empty_list = list()
# empty_set = set()

the_set = {"dog", "cat", "elephant"}
# Adding value to set
the_set.add("mouse")
# Removing set value
the_set.remove("mouse")

the_set.add('cat')
print(the_set)
# Example of actually using set for useful purpose
example_list = [1,1,1,1,1,1,2,2,2,2,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,5,5,5,5,5,5,5]
new_list =list(set(example_list))
new_list.reverse()
print(new_list)
