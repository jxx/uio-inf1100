from math import sqrt, pi, e
from pprint import pprint

def h(x):
    return (1/np.sqrt(2*np.pi)) * np.exp**(-0.5*x**2)

n = 41  # number of points along the x axis
x_start = -4.0
x_end = 4.0
dx = (x_end-x_start)/(n-1)


xlist = [i * dx for i in range((-n+1)/2, (n+1)/2)]
ylist = [h(x) for x in xlist]

pairs = [[x, y] for x, y in zip(xlist, ylist)]

pprint(xlist)


"""Array type solution"""
x = np.array(np.zeros)
y = np.array(np.zeros)

for i in range(num_values):
    x[i] = x_start + i * dx
    y[i] = h(x[i])
