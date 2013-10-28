Print 'Class notes 2013-10-21'

# For vectors: (0,1) + (3,4) = (3,5)

class Vec:
    #constructor to get the two vectors
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def write(self):
        print '(%g, %g)' % (self.x, self.y)

    def __str__(self):
        return '(%g, %g)' % (self.x, self.y)

    def __add__(self, other):
        """ Return self + other """

        return Vec(self.x + other.y,
                   self.y + other.y)
u = Vec(0,1)
v = Vec(3,4)
w = u + v
print w
#u.write()


