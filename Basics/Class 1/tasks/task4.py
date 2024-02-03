# 4. This equation x2 +  y2 +  z2 – 3xyz
# formula: (x + y + z)(x2 +  y2 +  z2 – xy – yz -xz)
print("What about the last equation? I will need 3 variables")
x = int(input("Give me an X: "))
y = int(input("Give me an Y: "))
z = int(input("Give me an Z: "))
result4 = (x + y + z) * (x**2 + y**2 + z**2 - x*y - y*z - x*z)

print("The result of the last one would be", result4)
