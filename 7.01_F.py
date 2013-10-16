""" Make a funtion class """
# clue: avoid global variables. 
from math import exp, sin

class GeneralFunction:
    def __init__(self, a=1.0, w=0):
        self.a = a
        self.w = w

    def value(self, x):
        return exp(-self.a*x)*sin(self.w*x)

OneInstanceOfAFunction = GeneralFunction(a=1, w=2) # F.__init__(f, a=1, w=2)
v = OneInstanceOfAFunction.value(-2)
print v
print type(OneInstanceOfAFunction)
print OneInstanceOfAFunction.__class__.__name__


# 7.4 og 7.5 er kritiske 
