# !/usr/bin/python

################################################
#       GUI using tkinter
#       Name : Jeremy
#       Date: 7 / 6 / 22
#  #############################################

from tkinter import *

window = tk()
window.title("Welcome to my code")
window.configure(bg = 'blue') # background color
window.geometry("700 x 600") # fix window size

# creating a label
f_name = Label(window, text = "First name", font = ("calibri",40)) # create the text
s_name = Label(window, text = "Second name", font = ("calibri",40))
f_name.grid(column = 30, row = 30) # gives location
s_name.grid(column = 30, row = 60)

# creating a button and giving it a function
def open_popup():
    top = Toplevel(window)
    top.geometry("300x300")
    top.title("Pop up window")
    top.configure(bg = 'orange')
    msg = Label(top, text = "Welcome to pop up", font = ("Times new roman", 18)).place(x = 150, y = 150)
btn = Button(window,text = "Log on", bg = 'green', fg = 'purple',command = open_popup().pack())
btn.grid(column = 170 , row = 170)

# crating text box
f_name_box = Entry(window, width = 25, height = 15)
f_name_box.grid(column = 45, row = 30) # should be on same row as first name label

s_name_box = Entry(window, width = 25, height = 15)
s_name_box.grid(column = 45, row = 60) # should be on same row as second name label


window.mainloop() 

# assignment create a clock. design school system