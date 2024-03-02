print("Hello world!")

variable1 = 15
variable2 = "String value qweqwe asdfbd zzve teste as test test etest"  # Create text
variable3 = 15.958774162
variable4 = True

# integer(int), float, string(str), boolean(bool), None, undefined
int(variable3)
float(variable1)
type(variable1)  # Getting a type of a variable

len(variable2)
new_words = []  # initiate empty list
for word in variable2.split():  # iterate through words
    new_words.append(word.strip('e'))  # append list with striped e from start and end of words

new_text = ' '.join(new_words)  # converting list to text
print(new_text)

list_variable = [{}, {}, {}]
dictionary = {'key': [{"key": [{}, {}]}]}

user_choice = input("Chose what to do: a;sdasdasd")

# 0, '', null, undefined, [], {} = Falsy
# 1, ' ', [0], {"key":"value"} = Truthy

if user_choice:
    print("This happens")

if user_choice:
    print("do True case things")
elif user_choice == "potato":
    print("Latvian Gold")
else:
    print("Do whatever for not accounted cases")

iterable_text = "asdadadasdasdasdaafgasf"

for letter in iterable_text:
    print(letter)

while True:
    number = int(input("asdasd"))
    if number < 5:
        break


#
# while True:
#     print("Potato")


def function_name(*args):
    sum = 0
    for arg in args:
        sum += arg
    print(sum)


function_name(1, 2, 3, 4, 5, 6, 7, 8, 9)

with open("test1.txt") as f:
    with open("test2.txt", "r+") as f2:
        print(f, f2)
