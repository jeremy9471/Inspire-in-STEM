# !/usr/bin/python

################################################
#       relating files
#       Name : Jeremy
#       Date: 6 / 6 / 22
#  #############################################
import operations # to call: operations: add_num(4,7) example
from students import Student
from teachers import Teachers
print(operations.prod_num(5,7))
print(operations.sub_num(6,3))
print(operations.add_num(5,6))
print(operations.prod_num(3,6))

new_student = Student("Jeremy","Travelling", "2003")
Student.greet_student()

new_teacher = Teachers("Joan", 123987 , "Literature" , 60000)
print(new_teacher.get_TSC_num())