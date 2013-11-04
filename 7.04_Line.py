"""
The class Line whose takes two points p1 and p2 (2-tuples or 2-lists) as input.

Usage:
myobject = Line((x0, y0), (x1, y1)) 

Methods:
    value(x) computes a value on the line at the point x.

iPython example:
>>> from Line import Line
>>> line = Line((0,-1), (2,4))
>>> print line.value(0.5), line.value(0), line.value(1)
0.25 -1.0 1.5
"""

class Line:
    """ Line object """
    def __init__(self, p1, p2):
        self.x0 = p1[0]
        self.y0 = p1[1]
        self.x1 = p2[0]
        self.y1 = p2[1]

    def value(self, x):
    """ Calculates the value at x """
        x0, y0, x1, y1 = self.x0, self.y0, self.x1, self.y1
        self.x = x

        a = (y1 - y0) / float(x1 - x0)
        b = y0 - a * x0
    
        return a * x + b

line = Line((0,-1), (2,4))

print line.value(0.5), line.value(0), line.value(1)

"""
$ python 7.04_Line.py 
0.25 -1.0 1.5
"""
