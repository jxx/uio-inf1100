"""
Gaussian2.py
Make a python function gauss(x, m=0, s=1) to calculate Gauss function
Call gauss(x) and print values for 11 equally spaced x in [-5,5]
"""

def gauss(x, m=0, s=1):
    from math import sqrt, pi, exp
    gauss = ( 1 / ( sqrt( 2 * pi ) * s )  ) * exp( ( -1./2. * ( (x-m) / s) ** 2 ) ) 
    return gauss

gauss_values = []

n = 11. # number of equally spaced values
x_min = -5
x_max = 5
dx = (x_max - x_min)/(n-1) # spacing of t values
x = x_min

print 'Printing f(x) for ' + str(int(n)) + ' steps from ' + str(x_min) + ' to ' + str(x_max)

while x <= x_max:
    value = gauss(x)
    gauss_values.append(value)
    print '%8.3f %8.3f' % (x, value)
    x += dx

"""
$ python 3.14_Gaussian2.py 
Printing f(x) for 11 steps from -5 to 5
  -5.000    0.000
  -4.000    0.000
  -3.000    0.004
  -2.000    0.054
  -1.000    0.242
   0.000    0.399
   1.000    0.242
   2.000    0.054
   3.000    0.004
   4.000    0.000
   5.000    0.000
"""
