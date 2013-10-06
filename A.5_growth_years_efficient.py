from scitools.std import *
x0 = 100.                     # initial amount
p = 5                         # interest rate
N = 4                         # number of years
n = 0

# Compute solution
x_prev = x0

while n < N:
    x_curr = x_prev + (p/100.0)*x_prev
    x_prev = x_curr
    print x_curr
    n += 1

"""
$ python A.5_growth_years_efficient.py 
105.0
110.25
115.7625
121.550625
"""
