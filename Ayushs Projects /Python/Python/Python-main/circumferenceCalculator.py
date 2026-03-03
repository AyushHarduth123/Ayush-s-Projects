import math

#simple code using the math import ot calculate area and circumference of a circle and the hypoth of a triangle 


radius = float(input("Enter the radius of the circle = "))

Circumf = float(2*(math.pi)*radius)

print(f"The circumference of the circle is = {round(Circumf,2)}cm")

area = float(math.pi * (pow(radius,2)))

print(f"The area of the circle is = {round(area, 2)}cm²")


# calculating the hypoth of a triangle 
a = float(input(f"Enter the lenth of a = "))
b = float(input("Enter the length of b = "))

c = math.sqrt(pow(a,2)+pow(b,2))

print(f"The hypothenus of the triangle is = {round(c,2)}cm")