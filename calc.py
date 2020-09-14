"""
Author = Fayemi Boluwatife

"""

import tkinter as tk
import math, tkmath
from tkinter import messagebox

root = tk.Tk()
root.configure(bg = "#262626")
root.title("Calculator")

def press(num):
    """ prints num clicked """
    global expression
    if expression == result or expression == "0":
        expression = ""
    expression += str(num)
##    print(expression)
    equation.set(expression)

def equalPress():
    """ prints the result of the calculation"""
    global expression
    global result
    result = str(eval(expression))
    expression = result
    equation.set(expression)
##    print(expression)

def operatorPress(operator):
    """ prints operator clicked """
    global expression
    if not expression.endswith(operators):
        expression += operator
##        print(expression)
        equation.set(expression)
    else:
        expression = expression[:-1] + operator
##        print(expression)
        equation.set(expression)
    
def delete():
    """ to delete the last character on screen """
    global expression
    if result != expression:
        #expression is manipulated to list so that pop() can be used
        deletedList = " ".join(expression).split(" ")
##        print(deletedList)
        deletedList.pop()
##        print(deletedList)
        expression = "".join(deletedList)
##        print(expression)
        equation.set(expression)
   
def reset():
    """to clear all the input values"""
    global expression
    expression = "0"
    equation.set(expression)

def aboutdev():
    message = messagebox.showinfo("About",
"""This calculator is developed by Fayemi Boluwatife.
Copyright 2020.
Bovage INC.""", icon = "info")
#=======================Variables==============================
equation = tk.StringVar()
equation.set("0")
expression = "0"
result = ""
operators = ("+", "-", "*", "/")

#===================Menu=======================================
menubar = tk.Menu(root)
menubar.add_command(label = "About", command = aboutdev)
root.config(menu = menubar)


#===================Menu=======================================
screenFrame = tk.Frame(root, bd = 2, width = 100, height = 200, bg = "white",
                       relief = "flat")
screenFrame.grid(row = 0, column = 0, pady = 5, padx = 5, ipadx = 0)

screen = tk.Label(screenFrame, bd = 2, width = 15, height = 3, textvariable = equation,
                  bg = "#1a1a1a", fg = "white", font = ("Arial", 20, "bold"),
                  relief = "raise", anchor = "e", wraplength = "256")
screen.grid(row = 0, column = 0)

buttonFrame = tk.Frame(root, bd = 2, width = 100, height = 300, bg = "#262626",
                       relief = "flat")
buttonFrame.grid(row = 1, column = 0, sticky = "W", padx = 5, pady = 5)

#==================buttons==================================================
buttonPercent = tk.Button(buttonFrame, width = 3, height = 1, text = "%",
                          font = ("Arial", 16, "bold"), fg = "white",
                          bg = "#1a1a1a", command = lambda: press("%"),
                          activebackground = "#262626")
buttonPercent.grid(row = 0, column = 0, padx = 1, pady = 1)


buttonroot = tk.Button(buttonFrame, width = 3, height = 1, text = "√", font = ("Arial", 16, "bold"),
                    fg = "white", bg = "#1a1a1a", command = lambda: tkmath.squroot(int(expression), equation),
                       activebackground = "#262626")
buttonroot.grid(row = 0, column = 1, padx = 1, pady = 1)

buttonSqu = tk.Button(buttonFrame, width = 3, height = 1, text = "x2", font = ("Arial", 16, "bold"),
                    fg = "white", bg = "#1a1a1a", command = lambda:tkmath.pow(int(expression), 2, equation),
                      activebackground = "#262626")
buttonSqu.grid(row = 0, column = 2, padx = 1, pady = 1)

buttonReciprocal = tk.Button(buttonFrame, width = 3, height = 1, text = "1/x", font = ("Arial", 16, "bold"),
                    fg = "white", bg = "#1a1a1a", activebackground = "#262626",
                             command = lambda: tkmath.reciprocal(int(expression), equation))
buttonReciprocal.grid(row = 0, column = 3, padx = 1, pady = 1)

buttonCE = tk.Button(buttonFrame, width = 3, height = 1, text = "CE", font = ("Arial", 16),
                    fg = "white", bg = "#1a1a1a", command = reset,
                     activebackground = "#262626")
buttonCE.grid(row = 1, column = 0, padx = 1, pady = 1)

buttonC = tk.Button(buttonFrame, width = 3, height = 1, text = "C", font = ("Arial", 16),
                    fg = "white", bg = "#1a1a1a", activebackground = "#262626")
buttonC.grid(row = 1, column = 1, padx = 1, pady = 1)

#"\u232B" is the unicode character for del
buttonDel = tk.Button(buttonFrame, width = 3, height = 1, text = "\u232B", font = ("Arial", 16),
                    fg = "white", bg = "#1a1a1a", command = delete,
                      activebackground = "#262626")
buttonDel.grid(row = 1, column = 2, padx = 1, pady = 1)

buttonDivider = tk.Button(buttonFrame, width = 3, height = 1, text = "÷", font = ("Arial", 16),
                    fg = "white", bg = "#1a1a1a",command = lambda: operatorPress("/"), activebackground = "#262626")
buttonDivider.grid(row = 1, column = 3, padx = 1, pady = 1)

button7 = tk.Button(buttonFrame, width = 3, height = 1, text = 7, font = ("Arial", 16, "bold"),
                    fg = "white", bg = "black", command = lambda: press(7),
                    activebackground = "#262626")
button7.grid(row = 2, column = 0, padx = 1, pady = 1)

button8 = tk.Button(buttonFrame, width = 3, height = 1, text = 8, font = ("Arial", 16, "bold"),
                    fg = "white", bg = "black", command = lambda: press(8),
                    activebackground = "#262626")
button8.grid(row = 2, column = 1, padx = 1, pady = 1)

button9 = tk.Button(buttonFrame, width = 3, height = 1, text = 9, font = ("Arial", 16, "bold"),
                    fg = "white", bg = "black", command = lambda: press(9),
                    activebackground = "#262626")
button9.grid(row = 2, column = 2, padx = 1, pady = 1)

buttonX = tk.Button(buttonFrame, width = 3, height = 1, text = "X", font = ("Arial", 16),
                    fg = "white", bg = "#1a1a1a", command = lambda: operatorPress("*"),
                    activebackground = "#262626")
buttonX.grid(row = 2, column = 3, padx = 1, pady = 1)

button4 = tk.Button(buttonFrame, width = 3, height = 1, text = 4, font = ("Arial", 16, "bold"),
                    fg = "white", bg = "black", command = lambda: press(4),
                    activebackground = "#262626")
button4.grid(row = 3, column = 0, padx = 1, pady = 1)

button5 = tk.Button(buttonFrame, width = 3, height = 1, text = 5, font = ("Arial", 16, "bold"),
                    fg = "white", bg = "black", command = lambda: press(5),
                    activebackground = "#262626")
button5.grid(row = 3, column = 1, padx = 1, pady = 1)

button6 = tk.Button(buttonFrame, width = 3, height = 1, text = 6, font = ("Arial", 16, "bold"),
                    fg = "white", bg = "black", command = lambda: press(6),
                    activebackground = "#262626")
button6.grid(row = 3, column = 2, padx = 1, pady = 1)

buttonminus = tk.Button(buttonFrame, width = 3, height = 1, text = "-", font = ("Arial", 16),
                    fg = "white", bg = "#1a1a1a", command = lambda: operatorPress("-"),
                        activebackground = "#262626")
buttonminus.grid(row = 3, column = 3, padx = 1, pady = 1)

button1 = tk.Button(buttonFrame, width = 3, height = 1, text = 1, font = ("Arial", 16, "bold"),
                    fg = "white", bg = "black", command = lambda: press(1),
                    activebackground = "#262626")
button1.grid(row = 4, column = 0, padx = 1, pady = 1)

button2 = tk.Button(buttonFrame, width = 3, height = 1, text = 2, font = ("Arial", 16, "bold"),
                    fg = "white", bg = "black", command = lambda: press(2),
                    activebackground = "#262626")
button2.grid(row = 4, column = 1)

button3 = tk.Button(buttonFrame, width = 3, height = 1, text = 3, font = ("Arial", 16, "bold"),
                    fg = "white", bg = "black", command = lambda: press(3),
                    activebackground = "#262626")
button3.grid(row = 4, column = 2, padx = 1, pady = 1)

buttonPlus = tk.Button(buttonFrame, width = 3, height = 1, text = "+", font = ("Arial", 16),
                    fg = "white", bg = "#1a1a1a", command = lambda: operatorPress("+"),
                       activebackground = "#262626")
buttonPlus.grid(row = 4, column = 3, padx = 1, pady = 1)

buttonPlusMinus = tk.Button(buttonFrame, width = 3, height = 1, text = "±", font = ("Arial", 16),
                    fg = "white", bg = "#1a1a1a", activebackground = "#262626")
buttonPlusMinus.grid(row = 5, column = 0, padx = 1, pady = 1)

button0 = tk.Button(buttonFrame, width = 3, height = 1, text = "0", font = ("Arial", 16, "bold"),
                    fg = "white", bg = "black", command = lambda: press(0),
                    activebackground = "#262626")
button0.grid(row = 5, column = 1, padx = 1, pady = 1)

buttonpoint = tk.Button(buttonFrame, width = 3, height = 1, text = ".", font = ("Arial", 16),
                       fg = "white", bg = "#1a1a1a", command = lambda: press("."),
                       activebackground = "#262626")
buttonpoint.grid(row = 5, column = 2, padx = 1, pady = 1)

buttonequal = tk.Button(buttonFrame, width = 3, height = 1, text = "=", font = ("Arial", 16),
                    fg = "white", bg = "#1a1a1a", command = equalPress,
                        activebackground = "#262626")
buttonequal.grid(row = 5, column = 3, padx = 1, pady = 1)

root.mainloop()
