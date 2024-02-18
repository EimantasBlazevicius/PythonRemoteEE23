class Car:
    def __init__(self, brand, fuel_tank, engine=1.6):
        self.brand = brand
        self.fuel = fuel_tank
        self.engine = engine

    def drive(self):
        self.fuel -= 10


car1 = Car("VW", 60)
car2 = Car("Opel", 55, 2)

car1.drive()
car2.drive()

print("This is car 1 fuel tank: ", car1.fuel)
print("This is car 2 fuel tank: ", car2.fuel)
