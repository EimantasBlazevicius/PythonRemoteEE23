sample_string = "Python 3.2"
numbers = 0
letters = 0

for char in sample_string:
    if char.isnumeric():
        numbers += 1
    elif char.isalpha():
        letters += 1

print("Letters:", letters)
print("Digits:", numbers)
