from timeit import timeit

setup = "from math import sqrt"

code = '''
def func():
    return [sqrt(x) for x in range(100)]
'''

print(timeit(stmt=code, setup=setup, number=200))
