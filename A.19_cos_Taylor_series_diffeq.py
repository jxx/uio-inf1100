import math
import numpy as np
from scitools.std import *

def cos_Taylor(x, N) :
    x = float(x)
    a_prev = 1
    s_prev = 0.0
    for j in range(1, N) :

        a_current = -x**2/((2*j)*j) * a_prev
        # a_current = -x**2/((2*j+1)*2*j) * a_prev

        s_current = s_prev + a_prev

        a_prev = a_current
        s_prev = s_current
        
    return s_prev

xmin = 0
xmax = 4*math.pi
ymin = -2
ymax = 2

xlist = np.linspace(xmin, xmax, 100) 
coslist = np.array([math.cos(x) for x in xlist]) #Exact cosine curve

for iterations in [1, 2, 3, 12, 60]:
    s = np.array([cos_Taylor(x, iterations) for x in xlist])
    plot(xlist, s,
         legend = ('Taylor, iterations=%d' % iterations),
         axis=[xmin, xmax, ymin, ymax])
    hold('on')
plot(xlist, coslist, legend = 'Exact')
