import sys
import numpy as np
from scitools.std import *
import time
import shutil, os

# Create temp subdir
subdir = 'temp' # subfolder name for plot files
if os.path.isdir(subdir): # does the subfolder already exist?
    shutil.rmtree(subdir) # delete the whole folder
os.mkdir(subdir) # make new subfolder
os.chdir(subdir) # move to subfolder

# ... perform all the plotting, make movie ...

savefile = sys.argv[0] + '.png'

def f(x,t):
    return e**-(x-3*t)**2 * sin(3*pi*(x-t))

x_range = np.linspace(-6, 6, 1001)
t_range = np.linspace(-1, 1, 11) # Exercise specifies 60+1, Devilry says 10

counter = 0
for t in t_range:
    y = f(x_range, t)
    plot(x_range, y, axis=[x_range[0], x_range[-1], -1, 1],
        xlabel='x', ylabel='f', legend='t=%4.2f' % t,
        savefig='tmp%04d.png' % counter)
    counter += 1
    time.sleep(0.2) # can insert a pause to control movie speed

# Make movie
movie('tmp*.png')

os.chdir(os.pardir) # optional: move up to parent folder

"""
$ python 5.22_plot_wavepacket_movie.py 



Found 61 files of the format tmp*.png.

scitools.easyviz.movie function runs the command: 

convert -delay 4 tmp*.png movie.gif



movie in output file movie.gif
"""
