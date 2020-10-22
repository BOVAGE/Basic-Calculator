"""
Author = Fayemi Boluwatife

"""

import tkinter as tk
import math
from tkinter import messagebox


class TkMath:
    def __init__(self):
        #self.equation textvariable what is been displayed on screen
        self.equation = tk.StringVar()
        self.equation.set("0")

        #self.expression stores what is being typed
        self.expression = "0"
        self.result = ""
        
    def pow(self,y, textvariable, updateX: bool = True):
        """ print the self.expression**y to the desired widjet. """
        answer = math.pow(float(self.expression),y)
        textvariable.set(answer)
        print(answer)
        if updateX:
            self.expression  = answer

    def squroot(self, textvariable, updateX: bool = True):
        """ print the sqr(self.expression) to the desired widjet. """
        answer = math.sqrt(float(self.expression))
        textvariable.set(answer)
        print(answer)
        if updateX:
            self.expression  = answer

    def reciprocal(self, textvariable, updateX: bool = True):
        """ print 1/self.expression to the desired widjet """
        try:
            answer = 1/self.expression
            textvariable.set(answer)
            print(answer)
            if updateX:
                self.expression  = answer
        except ZeroDivisionError:
            textvariable.set("Cannot divide by Zero")
        finally:
            print("Finally")

            
class Calc(TkMath):
    def __init__(self, window):
        super().__init__()
        self.operators: tuple = ("+", "-", "*", "/")
        
    #===================Menu=======================================
        menubar = tk.Menu(window)
        menubar.add_command(label = "About", command = self.aboutdev)
        window.config(menu = menubar)
        
    #===================Frames=======================================
        screenFrame = tk.Frame(window, bd = 2, width = 100, height = 200, bg = "white",
                               relief = "flat")
        screenFrame.grid(row = 0, column = 0, pady = 5, padx = 5, ipadx = 0)

        screen = tk.Label(screenFrame, bd = 2, width = 15, height = 3, textvariable = self.equation,
                          bg = "#1a1a1a", fg = "white", font = ("Arial", 20, "bold"),
                          relief = "raise", anchor = "e", wraplength = "256")
        screen.grid(row = 0, column = 0)

        buttonFrame = tk.Frame(window, bd = 2, width = 100, height = 300, bg = "#262626",
                               relief = "flat")
        buttonFrame.grid(row = 1, column = 0, sticky = "W", padx = 5, pady = 5)

    #==================buttons==================================================
        buttonPercent = tk.Button(buttonFrame, width = 3, height = 1, text = "%",
                                  font = ("Arial", 16, "bold"), fg = "white",
                                  bg = "#1a1a1a", command = lambda: self.press("%"),
                                  activebackground = "#262626")
        buttonPercent.grid(row = 0, column = 0, padx = 1, pady = 1)


        buttonroot = tk.Button(buttonFrame, width = 3, height = 1, text = "√", font = ("Arial", 16, "bold"),
                            fg = "white", bg = "#1a1a1a", command = lambda: self.squroot(self.equation),
                               activebackground = "#262626")
        buttonroot.grid(row = 0, column = 1, padx = 1, pady = 1)

        buttonSqu = tk.Button(buttonFrame, width = 3, height = 1, text = "x2", font = ("Arial", 16, "bold"),
                            fg = "white", bg = "#1a1a1a",
                              command = lambda:self.pow(2, self.equation),
                              activebackground = "#262626")
        buttonSqu.grid(row = 0, column = 2, padx = 1, pady = 1)

        buttonReciprocal = tk.Button(buttonFrame, width = 3, height = 1, text = "1/x", font = ("Arial", 16, "bold"),
                            fg = "white", bg = "#1a1a1a", activebackground = "#262626",
                                     command = lambda: self.reciprocal(self.equation))
        buttonReciprocal.grid(row = 0, column = 3, padx = 1, pady = 1)

        buttonCE = tk.Button(buttonFrame, width = 3, height = 1, text = "CE", font = ("Arial", 16),
                            fg = "white", bg = "#1a1a1a", command = self.reset,
                             activebackground = "#262626")
        buttonCE.grid(row = 1, column = 0, padx = 1, pady = 1)

        buttonC = tk.Button(buttonFrame, width = 3, height = 1, text = "C", font = ("Arial", 16),
                            fg = "white", bg = "#1a1a1a", activebackground = "#262626")
        buttonC.grid(row = 1, column = 1, padx = 1, pady = 1)

        #"\u232B" is the unicode character for del
        buttonDel = tk.Button(buttonFrame, width = 3, height = 1, text = "\u232B", font = ("Arial", 16),
                            fg = "white", bg = "#1a1a1a", command = self.delete,
                              activebackground = "#262626")
        buttonDel.grid(row = 1, column = 2, padx = 1, pady = 1)

        buttonDivider = tk.Button(buttonFrame, width = 3, height = 1, text = "÷", font = ("Arial", 16),
                            fg = "white", bg = "#1a1a1a",command = lambda: self.operatorPress("/"), activebackground = "#262626")
        buttonDivider.grid(row = 1, column = 3, padx = 1, pady = 1)

        button7 = tk.Button(buttonFrame, width = 3, height = 1, text = 7, font = ("Arial", 16, "bold"),
                            fg = "white", bg = "black", command = lambda: self.press(7),
                            activebackground = "#262626")
        button7.grid(row = 2, column = 0, padx = 1, pady = 1)

        button8 = tk.Button(buttonFrame, width = 3, height = 1, text = 8, font = ("Arial", 16, "bold"),
                            fg = "white", bg = "black", command = lambda: self.press(8),
                            activebackground = "#262626")
        button8.grid(row = 2, column = 1, padx = 1, pady = 1)

        button9 = tk.Button(buttonFrame, width = 3, height = 1, text = 9, font = ("Arial", 16, "bold"),
                            fg = "white", bg = "black", command = lambda: self.press(9),
                            activebackground = "#262626")
        button9.grid(row = 2, column = 2, padx = 1, pady = 1)

        buttonX = tk.Button(buttonFrame, width = 3, height = 1, text = "X", font = ("Arial", 16),
                            fg = "white", bg = "#1a1a1a", command = lambda: self.operatorPress("*"),
                            activebackground = "#262626")
        buttonX.grid(row = 2, column = 3, padx = 1, pady = 1)

        button4 = tk.Button(buttonFrame, width = 3, height = 1, text = 4, font = ("Arial", 16, "bold"),
                            fg = "white", bg = "black", command = lambda: self.press(4),
                            activebackground = "#262626")
        button4.grid(row = 3, column = 0, padx = 1, pady = 1)

        button5 = tk.Button(buttonFrame, width = 3, height = 1, text = 5, font = ("Arial", 16, "bold"),
                            fg = "white", bg = "black", command = lambda: self.press(5),
                            activebackground = "#262626")
        button5.grid(row = 3, column = 1, padx = 1, pady = 1)

        button6 = tk.Button(buttonFrame, width = 3, height = 1, text = 6, font = ("Arial", 16, "bold"),
                            fg = "white", bg = "black", command = lambda: self.press(6),
                            activebackground = "#262626")
        button6.grid(row = 3, column = 2, padx = 1, pady = 1)

        buttonminus = tk.Button(buttonFrame, width = 3, height = 1, text = "-", font = ("Arial", 16),
                            fg = "white", bg = "#1a1a1a", command = lambda: self.operatorPress("-"),
                                activebackground = "#262626")
        buttonminus.grid(row = 3, column = 3, padx = 1, pady = 1)

        button1 = tk.Button(buttonFrame, width = 3, height = 1, text = 1, font = ("Arial", 16, "bold"),
                            fg = "white", bg = "black", command = lambda: self.press(1),
                            activebackground = "#262626")
        button1.grid(row = 4, column = 0, padx = 1, pady = 1)

        button2 = tk.Button(buttonFrame, width = 3, height = 1, text = 2, font = ("Arial", 16, "bold"),
                            fg = "white", bg = "black", command = lambda: self.press(2),
                            activebackground = "#262626")
        button2.grid(row = 4, column = 1)

        button3 = tk.Button(buttonFrame, width = 3, height = 1, text = 3, font = ("Arial", 16, "bold"),
                            fg = "white", bg = "black", command = lambda: self.press(3),
                            activebackground = "#262626")
        button3.grid(row = 4, column = 2, padx = 1, pady = 1)

        buttonPlus = tk.Button(buttonFrame, width = 3, height = 1, text = "+", font = ("Arial", 16),
                            fg = "white", bg = "#1a1a1a", command = lambda: self.operatorPress("+"),
                               activebackground = "#262626")
        buttonPlus.grid(row = 4, column = 3, padx = 1, pady = 1)

        buttonPlusMinus = tk.Button(buttonFrame, width = 3, height = 1, text = "±", font = ("Arial", 16),
                            fg = "white", bg = "#1a1a1a", activebackground = "#262626")
        buttonPlusMinus.grid(row = 5, column = 0, padx = 1, pady = 1)

        button0 = tk.Button(buttonFrame, width = 3, height = 1, text = "0", font = ("Arial", 16, "bold"),
                            fg = "white", bg = "black", command = lambda: self.press(0),
                            activebackground = "#262626")
        button0.grid(row = 5, column = 1, padx = 1, pady = 1)

        buttonpoint = tk.Button(buttonFrame, width = 3, height = 1, text = ".", font = ("Arial", 16),
                               fg = "white", bg = "#1a1a1a", command = lambda: self.press("."),
                               activebackground = "#262626")
        buttonpoint.grid(row = 5, column = 2, padx = 1, pady = 1)

        buttonequal = tk.Button(buttonFrame, width = 3, height = 1, text = "=", font = ("Arial", 16),
                            fg = "white", bg = "#1a1a1a", command = self.equalPress,
                                activebackground = "#262626")
        buttonequal.grid(row = 5, column = 3, padx = 1, pady = 1)

    def press(self, num: int):
        """ prints num clicked """
        if self.expression == self.result or self.expression == "0":
            self.expression = ""
        self.expression += str(num)
        print(self.expression)
        self.equation.set(self.expression)

    def equalPress(self):
        """ prints the result of the calculation"""
        try:
            self.result = str(eval(self.expression))
            self.expression = self.result
            print(self.result)
            print("=====")
            print(self.expression)
            self.equation.set(self.expression)
        except ZeroDivisionError:
            self.equation.set("cannot divide by zero") 
        
##        print(self.expression)

    def operatorPress(self, operator: str):
        """ prints operator clicked """
        if not self.expression.endswith(self.operators):
            self.expression += operator
    ##        print(self.expression)
            self.equation.set(self.expression)
        else:
            self.expression = self.expression[:-1] + operator
    ##        print(expression)
            self.equation.set(self.expression)
        
    def delete(self):
        """ to delete the last character on screen """
        if self.result != self.expression:
            #expression is manipulated to list so that pop() can be used
            deletedList = " ".join(self.expression).split(" ")
            print(deletedList)
            deletedList.pop()
            print(deletedList)
            self.expression = "".join(deletedList)
            print(self.expression)
            self.equation.set(self.expression)
       
    def reset(self):
        """to clear all the input values"""
        self.expression = "0"
        self.equation.set(self.expression)

    def aboutdev(self):
        message = messagebox.showinfo("About",
    """This calculator is developed by Fayemi Boluwatife.
    Copyright 2020.
    Bovage INC.""", icon = "info")


def main():
    root = tk.Tk()
    root.configure(bg = "#262626")
    root.title("Calculator")
    calculator = Calc(root)
    root.mainloop()

if __name__ == "__main__":
    main()
