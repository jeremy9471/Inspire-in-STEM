# calculate area of a circle, volume and surface area of a cylinder and volume of a cube ( get user input)

# area of circle
radius = input("Enter radius of the circle ")
pi = 3.142
area = pi * int(radius) * int(radius)
print("The area of the circle is " + str(area))

# volume of cylinder
height = input("Enter height of the cylinder ")
baseRadius = input("Enter base radius of cylinder ")
volume = pi * int(baseRadius) * int(baseRadius) * int(height)
print("The volume of the cylinder is " + str(volume))

# surface area of the cylinder
surfaceArea = int(baseRadius) * 2 * pi * int(height)
print("The surface area of the cylinder is " + str(surfaceArea))


#volume of cube
length = input("Enter length of cube ")
volume = int(length) * int(length) * int(length)
print("Volume of the cube is " + str(volume))

#  surface area of a cube
surfaceAreaCube = int(length) * int(length) * 6
print("The surface area of the cube is " + str(surfaceAreaCube))