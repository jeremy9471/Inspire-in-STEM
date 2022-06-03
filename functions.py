# !/usr/bin/python

#################################
#       functions
#       Date: 31 / 5 / 22
#  ##############################
# function is a block of code executed together

# initializing a function
def say_hello():
    print("Hello from JKUAT ")
    x = 5
    y = 7
    z = x+y
    print(z)
say_hello()

# print function of sound made by 3 animals
def bark():
    print("Dogs bark")
bark()

# function parameters(what the function requires)
# function to add 2 numbers
def add_numbers(x,y):
    sum_nums = x+y
    print("The sum of the numbers is",sum_nums)
add_numbers(47,54)

# function for product of two numbers
def prod(x,y):
    product = x*y
    print("The product is",product)
prod(89,6)

# using default parameters
def print_name(name = "Jeremy"):    # print_name is the name of the function
    print(name)
print_name("Joseph")

# return from a function
def get_sum(num_1,num_2):
    sum_nums = num_1 + num_2
    return sum_nums
print(get_sum(76,98))

# write a function to get the powers of numbers
def powers(num,power):
    pow_num = num**power
    return pow_num
print(powers(6,4))

# print name
def get_full_name(f_name,s_name):
    full_name = f_name + " " + s_name
    return full_name.title()
print(get_full_name('Jeremy','Asugah'))