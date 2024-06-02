from collections import namedtuple, deque, ChainMap, Counter, OrderedDict, defaultdict

# namedtuple example
Variable = namedtuple('courses', 'course_name, language')
course = Variable('Algorithms', 'Python')
print(course)

# deque example
example_list = deque()
example_list.append(1)
example_list.append(2)
example_list.appendleft(3)
example_list.popleft()
print(list(example_list))

# chainmap example
b = {'music': 'bach', 'art': 'rembrandt'}
a = {'art': 'van gogh', 'opera': 'carmen'}
print(list(ChainMap(a, b)))

# Counter example
c = Counter("aaabbbgikkktjjfhvkhebhlsrgbh")
print(c)
l = Counter([1, 2, 3, 1, 2, 3, 5, 9, 9, 5, 1, 5])
print(l)
k = Counter(red=5, blue=2, yellow=1)
k2 = Counter(red=4, blue=1, yellow=1, orange=5)
print(list(k.elements()))
print(k.most_common(1))
k.update(k2)
print(k)

# Ordered dict
ordered_dictionary = OrderedDict()
ordered_dictionary[1] = 'a'
ordered_dictionary[2] = 'b'
ordered_dictionary[3] = 'c'
ordered_dictionary[4] = 'd'
ordered_dictionary[5] = 'e'
ordered_dictionary[6] = 'f'
ordered_dictionary[7] = 'g'

print(ordered_dictionary)
ordered_dictionary[1] = 'j'
print(ordered_dictionary)

# default dict
default = defaultdict(list)
default[1] = 'a'
default[2] = 'b'
print(default[5])
