# program to withdraw ksh 25000 if account balance is btw 100000 to 200000. 30% if account balance is btw 5000000 and 1m. above 1m, deduct 15000
balance = int(input("How much money do you have? "))
if (balance >=100000 and balance<=200000):
    newBalance = balance - 25000
    print(f"We have deducted 25000. Your new balance is {newBalance}.")
elif(balance>=500000 and balance<=1000000):
    newBalance = balance - (0.3 * balance)
    print(f"We have deducted 30%. Your newBalance is {newBalance}.")
elif(balance>1000000):
    newBalance = balance - 15000
    print(f"We have deducted 15000. Your new balance is {newBalance}.")
