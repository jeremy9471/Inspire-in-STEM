# !/usr/bin/python

#################################
#       Dictionaries
#       Name: Jeremy
#       Date: 23 / 5 / 22
#  ##############################


# Initializing dictionaries
# key value pairs
student = {"Name": "Jeremy", "Age": "18", "Gender": "Male"}
print(student["Name"])
print(student["Age"])
print(student["Gender"])

student["IdNo"] = "2054"
student["Club"] = "City"
print(student["IdNo"])
print(student)
student["x_position"] = 45
print(student)

# initialize empty dictionary
studentS = {}
studentS["favFood"] = "Chapatti"
studentS["homeCity"] = "Nakuru"
print(studentS)
# modify values
student["Age"] = "23"
print(student)
del student["Gender"]
print(student)