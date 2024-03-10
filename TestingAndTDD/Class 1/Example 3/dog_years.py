def get_dog_years(human_years):
    dog_years = 0

    for year in range(1, human_years + 1):
        if year < 3:
            dog_years += 10.5
        else:
            dog_years += 4

    return dog_years


if __name__ == "__main__":
    human_years = int(input("How many human years should we convert: "))
    print(get_dog_years(human_years))
    # (15, 73.0),(1, 10.5),(9,49.0),(7,41.0)
