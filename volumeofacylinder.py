import math
math.pi
pi = math.pi
radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))
volume = pi * radius **2 * height
print("The volume of the cylinder is", round(volume, 1))