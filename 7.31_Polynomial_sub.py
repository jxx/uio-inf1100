"""
Exercise 7.31. Implement subtraction of polynomials.
Implement the special method __sub__ in class Polynomial from
page 369. Name of program file: Polynomial_sub.py.

IMPORTANT EXERCISE - POLYNOMIAL EXERCISE WILL BE ON THE EXAM

"""

import numpy

class Polynomial:
    def __init__(self, coefficients):
        self.coeff = coefficients # USES A LIST

    def __call__(self, x):
        """Evaluate the polynomial."""
        s = 0
        for i in range(len(self.coeff)):
            s += self.coeff[i]*x**i # GENERAL ELEMENT, I IN THE LIST
        return s

    def __add__(self, other):
        """ Return Self + Other"""

        # IF TEST IMPORTANT: TWO CASES, 
        # Start with the longest list and add in the other
        # Self:   X X X X
        # Other:  X X X 0
        # Result: X X X X
        if len(self.coeff) > len(other.coeff):
            result_coeff = self.coeff[:]  # copy SELF!
            for i in range(len(other.coeff)):
                result_coeff[i] += other.coeff[i]
        else:
        # Self:   X X X 0
        # Other:  X X X X
        # Result: X X X X
            result_coeff = other.coeff[:] # copy OTHER!
            for i in range(len(self.coeff)):
                result_coeff[i] += self.coeff[i]
        return Polynomial(result_coeff)

    def __sub__(self, other):
        """ Return self-other """
        # Start with the longest list and add in the other

        if len(self.coeff) > len(other.coeff):
        # Self:   X X X X
        # Other:  X X X 0
        # Result: X X X X

            result_coeff = self.coeff[:]  # copy!
            for i in range(len(other.coeff)):
                result_coeff[i] -= other.coeff[i]
        else:
        # Self:   X X X 0
        # Other:  X X X X
        # Result: X X X X
            result_coeff = [0]*len(other.coeff)
#            result_coeff = other.coeff[:] # copy!
            for i in range(len(self.coeff)):
                result_coeff[i] = self.coeff[i] - self.other[i]
            for i in range(len(self.coeff), len(self.other)):
                result_coeff[i] -= other.coeff[i]
#    def __getitem__(self, i):
#        return self.coeff[1]:

        return Polynomial(result_coeff)

    def __mul__(self, other):
        c = self.coeff
        d = other.coeff
        M = len(c) - 1
        N = len(d) - 1
        result_coeff = numpy.zeros(M+N+1)
        for i in range(0, M+1):
            for j in range(0, N+1):
                result_coeff[i+j] += c[i]*d[j]
        return Polynomial(result_coeff)

    def differentiate(self):
        """Differentiate this polynomial in-place."""
        for i in range(1, len(self.coeff)):
            self.coeff[i-1] = i*self.coeff[i]
        del self.coeff[-1]

    def derivative(self):
        """Copy this polynomial and return its derivative."""
        dpdx = Polynomial(self.coeff[:])  # make a copy
        dpdx.differentiate()
        return dpdx

    def __str__(self):
        s = ''
        for i in range(0, len(self.coeff)):
            if self.coeff[i] != 0:
                s += ' + %g*x^%d' % (self.coeff[i], i)
        # Fix layout
        s = s.replace('+ -', '- ')
        s = s.replace('x^0', '1')
        s = s.replace(' 1*', ' ')
        s = s.replace('x^1 ', 'x ')
        #s = s.replace('x^1', 'x') # will replace x^100 by x^00
        if s[0:3] == ' + ':  # remove initial +
            s = s[3:]
        if s[0:3] == ' - ':  # fix spaces for initial -
            s = '-' + s[3:]
        return s

    def simplestr(self):
        s = ''
        for i in range(0, len(self.coeff)):
            s += ' + %g*x^%d' % (self.coeff[i], i)
        return s


def _test():
    p1 = Polynomial([1, -1])
    p2 = Polynomial([0, 1, 0, 0, -6, -1])
    p3 = p1 + p2
    print p1, '  +  ', p2, '  =  ', p3
    p4 = p1*p2
    print p1, '  *  ', p2, '  =  ', p4
    print 'p2(3) =', p2(3)
    p5 = p2.derivative()
    print 'd/dx', p2, '  =  ', p5
    print 'd/dx', p2,
    p2.differentiate()
    print '  =  ', p5
    p4 = p2.derivative()
    print 'd/dx', p2, '  =  ', p4

if __name__ == '__main__':
#    _test()
#    2 - x ** 3 + 0.5*x**4    [2, 0, 0, -3, 0.5] # Coeff list
#    1 + x - x**3             [1, 1, 0, -1] 


    p1 = Polynomial([2, 0, 0, -2, 0.5])
    p2 = Polynomial([1, 1, 0, -1])

    sub = p1 - p2

    print sub
