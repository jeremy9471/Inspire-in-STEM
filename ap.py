# !/usr/bin/python

#################################
#       arithmetic progressions
#       Date: 27 / 5 / 22
#  ##############################

# print first 10 terms of an ap. a is first term, d is the difference, n is the no. of terms
a = int(input("What is the first term? "))
d = int(input("What is the common difference? "))
n = int(input("What is the final term needed? "))
for i in range(1,n+1):
    n_term = a + (i-1)*d
    print(n_term)
s_n = (n/2)*((2*a)+(n-1)*d)
print(f"Sum of numbers is: {s_n}")
