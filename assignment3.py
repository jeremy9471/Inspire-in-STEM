# program to give sb 10000 if they are btw 25 and 30
# gender = input("What is your gender? male/female ")
age = input("How old are you? ")
accountBalance = 0
if (int(age)>25) and (int(age)<30):
    accountBalance = accountBalance+10000
    print("You have received ksh 10000")
else:
    print("Sorry no money for you")
 