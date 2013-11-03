""" Read any function and return the derivative """

class Derivative:
    """ Stores f and h as attributes and applies the differentiation 
    formula in the call special method. Returns the differential for a
    point, as a number
 
    Formula for numeric diff:
    f'(x) = (f(x-h) - f(x)) / h 
    """

    def __init__(self, f, h=1E-5):
        self.f = f
        self.h = float(h)

    def __call__(self):
        f, h = self.f, self.h
        return (f(x+h) - f(x))/h


from scitools.std import * #iseq
def trapezoidal(f, a, x, n):
    h = (x-a)/float(n)
    I = 0.5*f(a)
    for i in iseq(1, n-1):
        I += f(a + i*h)
    I += 0.5*f(x)
    I *= h
    return I

class Integral:
   def __init__(self, f, a, n=100):
       self.f, self.a, self.n = f, a, n
   def __call__(self, x):
       return trapezoidal(self.f, self.a, x, self.n) 

def f(x):
    return exp(-x**2)*sin(10*x)
a = 0; n = 200
F = Integral(f, a, n)
x = 1.2
print F(x)
