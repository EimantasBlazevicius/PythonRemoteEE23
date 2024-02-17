weight = float(input("What is your weight: "))
height = float(input("What is your height: "))

bmi = weight / (height ** 2)

if 0 < bmi <= 18.5:
    print("Underweight")
elif bmi <= 25.0:
    print("Normal")
elif bmi <= 30.0:
    print("Overweight")
elif bmi > 30:
    print("Obese")
