# half pyramids using nested for loop
rows = int(input("Enter number of rows: "))
for i in range(rows):
    for j in range(i+1):
        print("* ",end=" ")
    print("\n")

# full pyramid
rows = int(input("Enter no. of rows: "))
k = 0
for i in range(1,rows+1):
    for space in range(1,(rows-i)+1):
        print(end=" ")
    while k != (2*i-1):
        print("* ",end=" ")
        k+=1 # replacement for k=k+1
    k=0
    print()