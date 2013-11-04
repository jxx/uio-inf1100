"""
Class for quadratic functions.

Usage:
object = Quadratic(a, b, c)
a, b, and c are attributes for f (x; a, b, c) = ax^2 + bx + c.

Methods:
    value(x)       for computing a value of f at a point x,
    table(L, R, n) for writing out a table of x and f values for n x values in the interval [L, R]
    roots()        for computing the two roots.
"""

from scitools.std import *

class Quadratic:
    """ Class for calculating quadratic functions """
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def value(self, x):
        """ Computes f at point x. """
        return self.a * x**2 + self.b * x + self.c

    def table(self, L, R, n):
        """ Writes a table of x and f values for n x values in the interval [L, R]. """

        self.L, self.R, self.n =  L, R, n

        # Create array of x values from a to b in n steps:
        x_values = linspace(L, R, n)

        # Indices to traverse x
        index_set = range(len(x_values))

        # Create array of zeros for y values:
        y_values = zeros(len(x_values))
       
        # Assign f(x) values for each x value
        for i in index_set:
            y_values[i] = self.value(i)

        # Combine into one table
        return zip(x_values, y_values)


    def roots(self):
        """ Computes the two roots of the function. """
        a, b, c = self.a, self.b, self.c

        r1 = (-b + sqrt(b**2 - 4*a*c))/(2*a)
        r2 = (-b - sqrt(b**2 - 4*a*c))/(2*a)

        return r1, r2

# Tests
q = Quadratic(1, 4, 1)
x1, x2 = q.roots()
print x1, x2
print q.value(0)
print q.table(0, 10, 11)

"""
$ python 7.06_Quadratic.py 
-0.267949192431 -3.73205080757
1
[(0.0, 1.0), (1.0, 6.0), (2.0, 13.0), (3.0, 22.0), (4.0, 33.0), (5.0, 46.0), (6.0, 61.0), (7.0, 78.0), (8.0, 97.0), (9.0, 118.0), (10.0, 141.0)]
"""
