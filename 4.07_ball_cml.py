"""
Modify 4.6 such that v0 and t are read from the command line.
"""
import sys

t = float(sys.argv[1])
v0 = float(sys.argv[2])
g = 9.81

y = v0*t - 0.5*g*t**2
print y


"""
$ python 4.07_ball_cml.py 1 6
1.095
"""
