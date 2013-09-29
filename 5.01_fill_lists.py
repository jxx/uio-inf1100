from math import sqrt, pi, e
from pprint import pprint

def h(x):
    return (1/sqrt(2*pi)) * e**(-0.5*x**2)

n = 41  # number of points along the x axis
dx = 8.0/(n-1) # spacing between x points in [0,1]

xlist = [i * dx for i in range((-n+1)/2, (n+1)/2)]
ylist = [h(x) for x in xlist]

pairs = [[x, y] for x, y in zip(xlist, ylist)]

pprint(xlist)
