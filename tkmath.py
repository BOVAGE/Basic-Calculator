"""

Author = Fayemi Boluwatife

This module provides programmer the access to
use math module with tkinter

"""

import math

def pow(x, y, textvariable, widjet = "screen"):
    """ print the x**y to the desired widjet. """
    answer = math.pow(x,y)
    textvariable.set(answer)
    print(answer)

def squroot(x, textvariable):
    """ print the sqr(x) to the desired widjet. """
    answer = math.sqrt(x)
    textvariable.set(answer)
    print(answer)

def reciprocal(x, textvariable):
    """ print 1/x to the desired widjet """
    try:
        answer = 1/x
        textvariable.set(answer)
        print(answer)
    except ZeroDivisionError:
        textvariable.set("Cannot divide by Zero")
    finally:
        print("Finally")
        
    
