class Car:
    def __init__(self, brand, color, form):
        self.brand = brand
        self.color = color
        self.form = form

    def drive(self):
        print("My car is doing brum brum")


class FuelCar(Car):
    def __init__(self, brand, color, form, fuel_type):
        super().__init__(brand, color, form)
        self.fuel_type = fuel_type

    def drive(self):
        print("I drive and I burn diesel ha ha ha")


car1 = FuelCar("VW", "black", "Universal", "Diesel")
car1.drive()
print(car1.color)
