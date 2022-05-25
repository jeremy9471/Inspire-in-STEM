# program to give sb 10000 if they are btw 25 and 30
age = int(input("How old are you? "))
accountBalance = 0
gender = input("What is your gender? ")
if (age>25) and (age<30) and (gender == "female"):
    accountBalance = accountBalance+10000
    print("You have received ksh 10000")
else:
    print("Sorry no money for you")
 