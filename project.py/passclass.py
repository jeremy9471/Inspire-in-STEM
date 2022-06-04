# put the password generator in a class
import random
num_passwords = int(input("Enter number of passwords: "))
len_password = int(input("Enter length of passwords: "))
class Passwords:
    def __init__(self,email):
        self.email = email
password1 = Passwords(str(input("Enter your email address: ")))
print("Your passwords are here: ")
for pwd in range(num_passwords):
    passwords = ''
    for c in range(len_password):
        passwords += random.choice(password1.email)
    print(passwords)
