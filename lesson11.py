# !/usr/bin/python

################################################
#       checking divisibility
#       Name: 
#       Date: 30 / 5 / 22
#  #############################################

num = int(input("Enter the number: "))
if num%5==0 or num%7==0:
    print(f"The number {num} is divisible by 5 or 7")
else:
    print(f"The number {num} is neither divisible by 5 or 7")

# write a program to write numbers in reverse (700 becomes 007)
num = int(input("Enter number: "))
reverse = 0
while num != 0:
    digit = num%10
    reverse = reverse * 10 + digit
    num //=10
print(reverse)