# password generator (enabling a user to generate random passwords but using their input)
import random
print("Welcome to the password generator!")
character = str(input("Enter your E-mail address: "))
num_passwords = int(input("How many passwords do you want? "))
len_password = int(input("How many characters do you want in your password? "))
print("Here are your passwords! ")
for pwd in range(num_passwords):
    passwords = ''
    for c in range(len_password):
        passwords += random.choice(character)
    print(passwords)

# putting the password in a class
class Passwords:
    def __init__(self,email,phone_num):
        self.email = email
        self.phone_num = phone_num
pass_1 = Passwords(str(character),str(799365556))
for pwd in range(num_passwords):
    pass_1 = ''
    for c in range(len_password):
        pass_1 += random.choice(pass_1.email,pass_1.phone_num)
    print(pass_1)