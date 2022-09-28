#Computes the roots of a quadratic equation

# import complex math module
import cmath

a = int( input("Enter value of a : " ))  
b = int( input("Enter value of b : " ))  
c = int( input("Enter value of c : " ))  

# find the discriminant 
d = (b**2) - (4*a*c)

# find two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(sol1,sol2))