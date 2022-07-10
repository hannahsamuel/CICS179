# Take radius of a sphere and outputs the sphere's diameter, circumference, surface area, and volume
# Diameter = 2 × radius
# Circumference = diameter × π
# Surface Area = 4 × π × radius**2
# Volume = 4/3 × π × radius**3
import math
radius = float(input("Radius = "))
print("Diameter : ", radius*2)
print("Circumference: ", radius*2*math.pi)
print("Surface area = ", 4*math.pi*(radius*radius))
print("Volume = " , math.pi*(radius*radius*radius)*(4/3))
