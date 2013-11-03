print 'Class notes 2013-10-21'
# For vectors: (0,1) + (3,4) = (3,5)

class Vec:
    #constructor to get the two vectors
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def write(self):
        print '(%g, %g)' % (self.x, self.y)

    def __str__(self):
        # __str__ is a magic word for print
        return '(%g, %g)' % (self.x, self.y)

    def __add__(self, other):
        #__add__ is a magic word for +
        """ Return self + other """

        return Vec(self.x + other.y,
                   self.y + other.y)

    def __repr__(self):
        # Print object representation: repr(object)
        # v is Vel
        # v = eval(repr(v))
        # e.g. v = Vec(8,7)
        # Excat syntax that you need to represent a vector
        # repr should print what you need to create an instance of a class
        return 'Vec(%g, %g)' % (self.x, self.y)

    def __sub__(self, other):
        #__sub__ is a magic word for -
        """ Return self - other """

        return Vec(self.x - other.y,
                   self.y - other.y)

    def __mul__(self, other):
        #__mul__ is magic word for *
        """ Return scalar product of self and other"""
        return self.x * other.x + self.y * other.y

u = Vec(0,1)
v = Vec(3,4)
w = u + v
print w
#u.write()

w2 = u - v
print w2
a = eval(repr(w2))
print a, type(a), a.__class__.__name__
