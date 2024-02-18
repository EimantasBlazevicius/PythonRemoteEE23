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

id_counter = 0
entries = []

with open("entries.txt", "r+") as f:
    headers = f.readline()
    if headers == "":
        f.write("id,name,age,city,potato_count\n")
    else:
        records = f.readlines()
        for record in records:
            line = record.strip().split(",")
            entries.append(Entry(line[0], line[1], line[2], line[3], line[4]))
            id_counter = int(line[0])
last_id = id_counter

while True:
    user_action = input("a - Add an entry\n"
                        "v - View the entries\n"
                        "x - Exit and Save\n"
                        ": ")

    if user_action.lower() == "a":
        id_counter += 1
        entry = Entry(id_counter)
        entry.get_user_data()
        entries.append(entry)
    elif user_action.lower() == "v":
        for entry in entries:
            entry.announcement()
    elif user_action.lower() == "x":
        break

with open("entries.txt", "a") as f:
    for entry in entries:
        # if entry.id > last id already present int he file:
        if int(entry.id) > last_id:
            f.write(entry.form_entry())

print("Yeyy, saved")
