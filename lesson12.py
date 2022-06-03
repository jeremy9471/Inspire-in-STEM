# !/usr/bin/python

################################################
#       functions continuation
#       Date: 3 / 6 / 22
#  #############################################


# returning a dictionary from a function
def create_full_name(f_name,s_name):
    person = {'first': f_name,'second': s_name}
    return person
print(create_full_name("Jeremy","Asugah"))

# parsing a list in a function
def greet_friends(names):# names are a list
    for name in names:
        msg = "Hello " + name.title() + "!"
        print(msg)
friends = ["Atai","Lesley","Job","John"]
greet_friends(friends)