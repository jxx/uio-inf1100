"""
Classes for rectangles and triangles.

Usage:
    myobject = rectangle(x0, y0 , W , H) 
    where 
    x0, y0   = lower left corner
    W        = width
    H        = height

    myobject = triangle(x0, y0, x1, y1, x2, y2) 
    where the coordinate pairs specify the three vertices of the triangle.

Methods:
    area()           Returns area of geometric shape
    circumference()  Returns circumference of geometric shape
"""

from scitools.std import *

class Rectangle:
    """ Class for rectangles """
    def __init__(self, x0, y0, W, H):
        self.x0, self.y0, self.W, self.H = x0, y0, W, H

    def area(self):
    """ Returns the area """
        return self.W * self.H

    def circumference(self):
    """" Returns the circumference """
        return 2 * self.W + 2 * self.H

class Triangle:
    """ Class for triangles """
    def __init__(self, x0, y0, x1, y1, x2, y2):
        self.x0, self.y0, self.x1, self.y1, self.x2, self.y2 = x0, y0, x1, y1, x2, y2

    def area(self):
    """ Returns the area """
        x0, y0, x1, y1, x2, y2 = self.x0, self.y0, self.x1, self.y1, self.x2, self.y2        

        return 0.5 * abs( 
            x1 * y2 -
            x2 * y1 -
            x0 * y2 +
            x2 * y0 +
            x0 * y1 -
            x1 * y0
            )

    def circumference(self):
    """" Returns the circumference """
        x0, y0, x1, y1, x2, y2 = self.x0, self.y0, self.x1, self.y1, self.x2, self.y2

        return (sqrt( (x1-x0)**2 + (y1-y0)**2 ) + \
                sqrt( (x2-x1)**2 + (y2-y1)**2 ) + \
                sqrt( (x1-x2)**3 + (y0-y2)**2 ))

# Tests:
r = Rectangle(0, 0, 2, 4)
print 'A rectangle at (%g, %g) with width %g and height %g has area %g and circumference %g ' % \
(r.x0, r.y0, r.W, r.H, r.area(), r.circumference())

t = Triangle(0, 0, 1, 0, 1, 2)
print 'A triangle with vertices (%g, %g), (%g, %g), (%g, %g) has area %g and circumference %g' % \
(t.x0, t.y0, t.x1, t.y1, t.x2, t.y2, t.area(), t.circumference())

"""
$ python 7.03_geometric_shapes.py 
A rectangle at (0, 0) with width 2 and height 4 has area 8 and circumference 12 
A triangle with vertices (0, 0), (1, 0), (1, 2) has area 1 and circumference 5
"""
