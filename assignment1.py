# calculate area of a circle, volume and surface area of a cylinder and volume of a cube ( get user input)

# area
radius = input("Enter radius of the circle ")
pi = 3.142
area = pi * int(radius) * int(radius)
print("The area of the circle is " + str(area))

# volume
height = input("Enter height of the cylinder ")
volume = area * int(height)
print("The volume of the cylinder is " + str(volume))

# surface area
circumfrence = int(radius) * 2 *pi
surfaceArea = int(circumfrence) * int(height)
print("The surface area of the cylinder is " + str(surfaceArea))


#volume of cube
length = input("Enter length of cube ")
volume = int(length) * int(length) * int(length)
print("Volume of the cube is " + str(volume))