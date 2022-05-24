# loops
school = ["Joy", "Bob", "Mercy","Happy"]
pupil = ["Mark", "Peace", "Hope", "Theo"]
# for pupil in pupil:
    # print(f"Hello I am {pupil}")

print("Number\tSquare")
print("================")
for number in range(0,10):
    print(number)
    print(number**2)

# print a diamond of stars
# a triangle of stars
n = int(input("enter rows: "))
m = (2*n) - 2
for i in range(0,n):
    for j in range(0,m):
        print(end =" ")
    m = m-1
    for j in range(0,i+1):
        print("*",end='')
    print(" ")