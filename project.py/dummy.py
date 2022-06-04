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

