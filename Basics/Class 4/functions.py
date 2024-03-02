# No return, no parameters
def test_function():
    print("Hello from the function!")


# Returns sum of 2+2, no parameters
def calculator():
    sum_of_two = 2 + 2
    return sum_of_two
    # a print function that will never run as it is unreachable
    print("Hello from the function!")


# No parameters, returns value
def conditional():
    if 5 < 3:
        return "Yes"
    else:
        return "No"


# takes parameter, return value, default value
def better_conditional(number=18):
    if number < 18:
        return "Go Home"
    return "You can come in"


# Has parameters, returns value
def calculator_two(number2, number1=9):
    result = number1 + number2
    return result


# test_function()
# result = calculator()
# value = conditional()
# print(value)
# number99 = 99
# number7 = 7
# result = calculator_two(number99, 7)
# print(result)
print(better_conditional())
