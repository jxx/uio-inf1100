from math import exp, sin, pi

class F:
    def __init__(self, a, w):
        self.a = a
        self.w = w

    def value(self, x): # Silly solution, use __call__
        return exp(-self.a*x)*sin(self.w*x)

    def __call__(self, x):
        return exp(-self.a*x)*sin(self.w*x)

f = F(1, 0.1)

print f(pi)

f.a = 2
print f(pi)

quit()
myfunction = F(a=1, w=2)    # What happens? F.__init__(myfunction, a=1, w=2)
v = myfunction.value(x=2)
print v
print type(myfunction)  # not informative
print myfunction.__class__.__name__
myfunction.a = 2
print myfunction.value(2)  # self.a is 2
