human_years = int(input("How many human years should we convert: "))
dog_years = 0

for year in range(1, human_years + 1):
    if year < 3:
        dog_years += 10.5
    else:
        dog_years += 4

print(dog_years)
