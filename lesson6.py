# lists
motorcycleOwner = "Mojo Jojo"
plateNumber = ["H1234", "Y1234", "S1234"]
motorcycle = ["Honda", "Yamaha", "Suzuki"]
# accessing items in a list using index
# print(motorcycle[0])

# changing data in a list
# motorcycle[1]= "Bugatti"
# print("I love " + motorcycle[1])

# adding elements in a list append
motorcycle.append("Bugatti")
# print(motorcycle)

# each motorcycle with its plate number
# print(motorcycle[0], plateNumber[0], motorcycle[1], plateNumber[1], motorcycle[2], plateNumber[2])

# removing items from a list, del
# del motorcycle[0]
# print(motorcycle)
# pop removes last index
popped_motorcycle = motorcycle.pop()
# print(popped_motorcycle)

print("My name is " + motorcycleOwner + " and i own a " + motorcycle[1] + plateNumber[1])
print(f"My name is {motorcycleOwner} and I own a {motorcycle[1]} {plateNumber[1]}")
# removing an item from a list
motorcycle.remove("Suzuki")
print(motorcycle)