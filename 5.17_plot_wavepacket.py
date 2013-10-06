import sys
import numpy as np
from scitools.std import *
savefile = sys.argv[0] + '.png'

def f(x,t):
    return np.exp**-(x-3*t)**2 * np.sin(3*pi*(x-t))

t = 0
x_range = np.linspace(-4, 4, 1000)
y_range = np.array([f(x,t) for x in x_range])

plot(x_range, y_range)
savefig(savefile)
print 'Plot saved as', savefile

"""
$ python 5.17_plot_wavepacket.py 
Plot saved as 5.17_plot_wavepacket.py.png
""" 
