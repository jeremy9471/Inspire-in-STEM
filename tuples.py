# !/usr/bin/python

################################################
#       tuples
#       Date: 31 / 5 / 22
#  #############################################

# lists and dictionaries can be edited, tuples cannot. They use normal brackets
fruits = ('mango','guava','banana','lime')
#fruits[1] = 'pineapple' items in a tuple cannot be changed
print(fruits[1])

cars = ('audi','bmw','vw','toyota')
cars = ('nissan','bmw','vw','toyota')

fav_foods = ('fries','chicken','chapatti','rice')
for fav_food in fav_foods:
    print(fav_food)