class Entry:
    def __init__(self, id, name='', age='', city='', potato_count=''):
        self.id = id
        self.name = name
        self.age = age
        self.city = city
        self.potato_count = potato_count

    def form_entry(self):
        return f"{self.id},{self.name},{self.age},{self.city},{self.potato_count}\n"

    def get_user_data(self):
        print("Provide the following information please: ")
        self.name = input("Name: ")
        self.age = input("Age: ")
        self.city = input("City: ")
        self.potato_count = input("Potato Count: ")

    def announcement(self):
        print(f"The participant {self.name}, aged {self.age} years old, coming from {self.city} have "
              f"destroyed {self.potato_count} potatoes yesterday.")


print("Hello to the great annual Potato eating competition!")

id_counter = 1
entries = []

while True:
    user_action = input("a - Add an entry\n"
                        "v - View the entries\n"
                        "x - Exit and Save\n"
                        ": ")

    if user_action.lower() == "a":
        entry = Entry(id_counter)
        entry.get_user_data()
        entries.append(entry)
        id_counter += 1
    elif user_action.lower() == "v":
        for entry in entries:
            print(entry.announcement())
    elif user_action.lower() == "x":
        break

# with open("entries.txt", "x") as f:
#     f.write("id,name,age,city,potato_count\n")

with open("entries.txt", "a") as f:
    for entry in entries:
        f.write(entry.form_entry())
