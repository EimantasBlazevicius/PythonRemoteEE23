class RocketShip:
    def __init__(self, fuel, length):
        self.fuel = fuel
        self.length = length

    def __gt__(self, other):
        return self.length > other.length

    def __eq__(self, other):
        return self.fuel == other.fuel


rocket1 = RocketShip(1700, 50)
rocket2 = RocketShip(1700, 45)

print(rocket1 < rocket2)
print(rocket1 == rocket2)

print('Some text in qoutes "asdasdad" ')
