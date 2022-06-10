# !/usr/bin/python

################################################
#       checking palindromes
#       Name: 
#       Date: 8 / 6 / 22
#  #############################################

s = input("Enter the word or number you wish to check: ")
def palindrome(s):
    rev = ''.join(reversed(s)) # get the reverse of s
    if (s == rev):
        print(f"{s} is a palindrome")
    else:
        print(f"{s} is not a palindrome")
palindrome(s) 