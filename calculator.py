# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 20:48:21 2022

@author: デイン　メッタム 
"""

from tkinter import * 
from math import sqrt 

root = Tk() 
root.title("Simple Calculator") 
 
e = Entry(root, width=35, borderwidth=3) 
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10) 

    
#e.insert(0, "Enter Your Name: ") 

def button_click(number):
    current = e.get()
    e.delete(0, END) 
    e.insert(0, str(current) + str(number))
    
def button_add():
    firstNumber = e.get() 
    global f_num 
    global f_oper
    f_num = int(firstNumber) 
    f_oper = "addition" 
    e.delete(0, END) 
    
def button_subtract():
    firstNumber = e.get()  
    global f_num 
    global f_oper
    f_num = int(firstNumber) 
    f_oper = "subtraction" 
    e.delete(0, END) 

def button_multiply():
    firstNumber = e.get()  
    global f_num 
    global f_oper
    f_num = int(firstNumber) 
    f_oper = "multiplication" 
    e.delete(0, END) 

def button_divide():
    firstNumber = e.get()  
    global f_num 
    global f_oper
    f_num = int(firstNumber) 
    f_oper = "division" 
    e.delete(0, END) 
    
def button_square():
    firstNumber = e.get()  
    global f_num 
    f_num = int(firstNumber) * int(firstNumber) 
    e.delete(0, END) 
    e.insert(0, f_num)
    
def button_root():
    firstNumber = e.get()  
    global f_num 
    #f_num = pow(firstNumber, 0.5) 
    f_num = sqrt(int(firstNumber))
    e.delete(0, END) 
    e.insert(0, f_num)
    
def button_inverse():
    firstNumber = e.get()  
    global f_num 
    f_num = 1 / int(firstNumber) 
    e.delete(0, END) 
    e.insert(0, f_num)

def button_equal():
    secondNumber = e.get() 
    e.delete(0, END) 
    if f_oper == "addition":
        e.insert(0, f_num + int(secondNumber)) 
    elif f_oper == "subtraction":
        e.insert(0, f_num - int(secondNumber)) 
    elif f_oper == "multiplication":
        e.insert(0, f_num * int(secondNumber))
    else:
        e.insert(0, f_num / int(secondNumber))

def button_clear(): 
    f_num = 0     
    e.delete(0, END) 


# define buttons
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))

button_add = Button(root, text="+", padx=39, pady=20, command=button_add)
button_subtract = Button(root, text="-", padx=40, pady=20, command=button_subtract)
button_multiply = Button(root, text="*", padx=40, pady=20, command=button_multiply)
button_divide = Button(root, text="/", padx=40, pady=20, command=button_divide)

button_square = Button(root, text="x^2", padx=32, pady=20, command=button_square)
button_root = Button(root, text="sqrt(x)", padx=26, pady=20, command=button_root) 
button_inverse = Button(root, text="1/x", padx=34, pady=20, command=button_inverse) 

button_equal = Button(root, text="=", padx=87, pady=20, command=button_equal)
button_clear = Button(root, text="clear", padx=79, pady=20, command=button_clear)


# put buttons on screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_equal.grid(row=4, column=1, columnspan=2) 
button_clear.grid(row=5, column=1, columnspan=2)  

button_add.grid(row=5, column=0) 
button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2) 

button_square.grid(row=7, column=0)
button_root.grid(row=7, column=1)
button_inverse.grid(row=7, column=2)



root.mainloop()  
