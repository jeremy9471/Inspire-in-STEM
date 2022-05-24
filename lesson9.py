# !/usr/bin/python

#################################
#       loops with lists
#       Name: 
#       Date: 24 / 5 / 22
#  ##############################

squares = []
for number in range(0,10):
    square = number**2
    squares.append(square)
print(squares)

# cubes
cubes = []
for number in range(0,10):
    cube = number**3
    cubes.append(cube)
print(cubes)

# sum of numbers btw 1 and 100
sum = 0
for number in range(0,100):
    sum = sum+number
print(sum)

# if statements
age = 17
if age >= 18:
    print("Allowed to drive")
else:
    print("Too young to drive")

