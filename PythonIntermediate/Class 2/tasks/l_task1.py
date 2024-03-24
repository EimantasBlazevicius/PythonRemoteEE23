my_list = ["rotor", "level", "radar", "mama"]

result = list(filter(lambda x: (x == x[::-1]), my_list))

print(result)
