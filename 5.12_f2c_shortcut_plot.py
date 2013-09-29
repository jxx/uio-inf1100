import sys
import numpy as np
from scitools.std import *
savefile = sys.argv[0] + '.png'

def C(F):
    return (F - 32) * (5.0 / 9)

def C_approx(F):
    return (F - 30.) / 2

F_range = np.linspace(-20, 120)
C_range = np.array([C(F) for F in F_range])
C_approx_range = np.array([C_approx(F) for F in F_range])


plot(F_range, C_range, F_range, C_approx_range, 
     xlabel='Farenheit (F)', ylabel='Centigrade (F)')
legend('Exact','Approx')
savefig(savefile)
print 'Plot saved as', savefile

"""
$ python 5.12_f2c_shortcut_plot.py 
Plot saved as 5.12_f2c_shortcut_plot.py.png
""" 
