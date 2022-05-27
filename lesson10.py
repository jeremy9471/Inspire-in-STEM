# !/usr/bin/python

################################################
#       loops and conditional statements
#       Name: 
#       Date: 27 / 5 / 22
#  #############################################

# for loops(printing even numbers)
for number in range(0,20):
    if (number % 2 == 0):
        print(number)

# sum of even numbers from 0 to 20
sum = 0
for number in range(0,20):
    if (number %2==0):
        sum = sum + number
print(sum) 

# product of odd numbers between 0 and 10
prod = 1
for number in range(1,10):
    if (number %2 ==1):
        prod = prod * number
print(prod)

# calculate factorial of 6(for loop)
product = 1
for number in range(1,7):
    product = product * number
print(product)

# factorial of 9 (using while)
numNi = 9
prodNi = 1
while numNi>1:
    prodNi = prodNi * numNi
    numNi = numNi - 1
print(prodNi)


# while loop
num = 0 
while (num<10):
    if num%2 == 0:
        print(num)
    num = num +1
