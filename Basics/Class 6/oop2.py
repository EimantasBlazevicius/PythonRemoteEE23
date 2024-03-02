class Car:
    def __init__(self, brand, fuel_tank, speed, engine=1.6):
        self.brand = brand
        self.fuel = fuel_tank
        self.engine = engine
        self.speed = speed

    def __str__(self):
        return f"Brand: {self.brand}, {self.fuel}l in the tank, current speed {self.speed}"


car1 = Car("VW", 60, 90)
car2 = Car("Opel", 55, 78, 2)

print(car1)
print(car2)
