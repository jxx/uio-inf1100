import math
import numpy as np
from scitools.std import *

def sine_Taylor(x, N) :
    x = float(x)
    a_prev = x
    s_prev = 0.0
    for j in range(1, N) :
        a_current = -x**2/((2*j+1)*2*j)*a_prev
        s_current = s_prev + a_prev

        a_prev = a_current
        s_prev = s_current
        
    return s_prev

xmin = 0
xmax = 4*math.pi
ymin = -2
ymax = 2

xlist = np.linspace(xmin, xmax, 100) 
sinelist = np.array([math.sin(x) for x in xlist]) #Exact sine curve

for iterations in [1, 2, 3, 6, 12]:
    s = np.array([sine_Taylor(x, iterations) for x in xlist])
    plot(xlist, s,
         legend = ('Taylor, iterations=%d' % iterations),
         axis=[xmin, xmax, ymin, ymax])
    hold('on')
plot(xlist, sinelist, legend = 'Exact')

savefile = sys.argv[0] + '.png'
savefig(savefile)
print 'Plot saved as', savefile

"""
$ python 5.21_plot_Taylor_sin.py
Plot saved as 5.21_plot_Taylor_sin.py.png
"""
