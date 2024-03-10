cars = ["VW", "Audi", "BMW"]
# Adding values to the list
cars.append("Zap")
cars.append("Cupra")
# Joining lists
cars.extend(["Nissan", "Volvo", "Opel", "VW"])
# Length of cars list
print(f"Cars in the list {len(cars)}")
# Sort the list
cars.sort()
# Get a count of certain cars
print(f'Amount Volkswagen in the list: {cars.count("VW")}')
# Get the index of certain record
index_of_cupra = cars.index("Cupra")
print(f"The index of Cupra in this list is: {index_of_cupra}")
# Inserting at a certain index
cars.insert(index_of_cupra, "Opel")
print(cars)
# Remove item form the list at the index
deleted_item = cars.pop(index_of_cupra)
# Remove the last item form the list
cars.pop()
# Reverse the list
cars.reverse()
# Clear the list
cars.clear()

print(cars)
