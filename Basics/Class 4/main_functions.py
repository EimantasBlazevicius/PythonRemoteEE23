def greet(name):
    print(f"Welcome to potato eating registry {name}!")


def get_action():
    print()
    print("Options are:")
    print("1 - Add new entry")
    print("2 - Display all the entries")
    print("3 - Exit the program")
    user_input = input("Chose your action: ")

    return user_input


def get_entry_details():
    print()
    name = input("Please state your name: ")
    age = input("Please state your age: ")
    city = input("Where are you from: ")
    amount_of_potatoes = input("How many potatoes did you down yesterday?: ")
    print(f"Thanks {name} your record of {amount_of_potatoes} potatoes eaten is now recorded!")

    return f"The participant {name}, aged {age} years old, coming from {city} have destroyed {amount_of_potatoes} potatoes yesterday."


def show_entries(entries):
    print()
    for entry in entries:
        print(entry)


if __name__ == "__main__":
    greet("Some Random Text")
    show_entries(['text', 'text2'])
