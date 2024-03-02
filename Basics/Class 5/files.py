# "r" - read mode (default value).
# "w" - write mode.
# "x" - creation mode. If the file already exists, the operation fails.
# "a" - appending mode.
# "b" - binary mode.
# "t" - text mode (default value).
# "+" - updating mode (read / write).

# f = open("example.txt", "r+")
# print(f.readline())
# f.close()

with open("example.txt", "r+") as f:
    print(f)
    # f.write("\nLines")
    # f.writelines(["some\n", "New\n", "Text\n", "TO\n", "FILE\n"])
    keys = f.readline().strip().split(',')  # [name, surname, age, potatos]
    lines = f.readlines()  # ["Eimantas,Blazevicius,30,99\n", "Mantas,Blazevicius,27,159\n"]
    my_people = []
    for line in lines:
        person = line.strip().split(",")  # ["Eimantas","Blazevicius","30","99"]
        person_dict = {}
        for index, attribute in enumerate(person):
            person_dict[keys[index]] = attribute
        my_people.append(person_dict)

print(my_people)
