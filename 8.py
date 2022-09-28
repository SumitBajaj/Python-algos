#Compute the volume of a cylinder given its length and diameter

import math
#take radius of the base of  a cylinder 
r=float(input("Enter r of a cylinder: "))
#take height of the curve surface of a cylinder 
h=float(input("Enter the Height of a cylinder: "))

#calculate the surface area of cylinder
s_area=2*math.pi*pow(r,2)*h

#calculate the volume of cylinder
volume=math.pi*pow(r,2)*h

print("surface area of a cylinder wll be %.2f" %s_area)
print("volume of a cylinder will be  %.2f" %volume)