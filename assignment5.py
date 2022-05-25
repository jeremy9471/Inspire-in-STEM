# !/usr/bin/python

#################################
#       lists and if
#       Name: 
#       Date: 25 / 5 / 22
#  ##############################


# create list of vehicles with: BMW,Audi,Toyota,Mercedes,Jeep. Use if to find jeep and convert to uppercase
vehicles = ["bmw", "audi", "toyota", "mercedes", "jeep"]

# print upper for each
for vehicle in vehicles:
    if vehicle == "jeep":   # locate the word jeep in the list
        print(vehicle.upper())
    else:
        print(vehicle.title())

# = sign: != - not equal to, == - is. eg if age !=16..., if age ==16....

# checking for users in a list
banned = ["Marie", "Anne"]
user = "Dave"
if user not in banned:
    print(f"{user},you can use the services")