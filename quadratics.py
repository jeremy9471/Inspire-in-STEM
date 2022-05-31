# create a function to find the roots of a quadratic eqution

import math

a = int(input("Enter coefficient of 1st term: "))
b = int(input("Enter coefficient of 2nd term: "))
c = int(input("Enter the constant: "))
w = math.sqrt((b**2)-(4*a*c))

def roots(a,b,c):
    x_1 = (-b + w)/(2*a)
    x_2 = (-b - w)/(2*a)
    print("The roots are:",x_1,x_2)
roots(a,b,c)