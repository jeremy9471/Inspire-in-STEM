# geometric progressions
a = int(input("Enter the first number: "))
r = int(input("What is the common ratio? "))
n = int(input("What is the final needed term? "))
for i in range(1,n+1):
    n_term = a*(r**(n-1))
    print(n_term)