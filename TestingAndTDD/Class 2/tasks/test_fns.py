import fns


# Task 1: Write a function to add two numbers
def test_is_isogram():
    assert fns.is_isogram("Dermatoglyphics") == True
    assert fns.is_isogram("isogram") == True
    assert fns.is_isogram("aba") == False
    assert fns.is_isogram("moOse") == False
    assert fns.is_isogram("isIsogram") == False
    assert fns.is_isogram("") == True


# Task 2: Write a function to check if a number is prime
def test_is_prime():
    assert fns.is_prime(2) == True
    assert fns.is_prime(10) == False
    assert fns.is_prime(17) == True


# Task 3: Write a function to reverse a string
def test_reverse_string():
    assert fns.reverse_string("hello") == "olleh"
    assert fns.reverse_string("python") == "nohtyp"
    assert fns.reverse_string("") == ""


# Task 4: Write a function to check if a string is a palindrome
def test_is_palindrome():
    assert fns.is_palindrome("radar") == True
    assert fns.is_palindrome("python") == False
    assert fns.is_palindrome("") == True


# Task 5: Write a function to calculate the factorial of a number
def test_factorial():
    assert fns.factorial(5) == 120
    assert fns.factorial(0) == 1
    assert fns.factorial(1) == 1


# Task 6: Write a function to find the maximum element in a list
def test_find_max():
    assert fns.find_max([1, 5, 3, 9, 2]) == 9
    assert fns.find_max([-10, -5, -20, -3]) == -3
    assert fns.find_max([]) == None


# Task 7: Write a function to check if a year is a leap year
def test_is_leap_year():
    assert fns.is_leap_year(2020) == True
    assert fns.is_leap_year(1900) == False
    assert fns.is_leap_year(2000) == True


# Task 8: Write a function to remove duplicates from a list
def test_remove_duplicates():
    assert fns.remove_duplicates([1, 2, 3, 2, 1, 5]) == [1, 2, 3, 5]
    assert fns.remove_duplicates([]) == []
    assert fns.remove_duplicates([1, 1, 1, 1, 1]) == [1]


# Task 9: Write a function to check if two strings are anagrams
def test_are_anagrams():
    assert fns.are_anagrams("listen", "silent") == True
    assert fns.are_anagrams("hello", "world") == False
    assert fns.are_anagrams("python", "typhon") == True


# Task 10: Write a function to convert Celsius to Fahrenheit
def test_celsius_to_fahrenheit():
    assert fns.celsius_to_fahrenheit(0) == 32.0
    assert fns.celsius_to_fahrenheit(100) == 212.0
    assert fns.celsius_to_fahrenheit(-40) == -40.0
