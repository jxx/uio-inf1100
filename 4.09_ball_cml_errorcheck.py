"""
Exercise 4.9. 
Test if the t value read in the program from Exercise 4.7 lies between
0 and 2v0 /g . If not, print a message and abort execution. Name of
program file: ball_cml_errorcheck.py.
"""

import sys


try:
    t = float(sys.argv[1])
    v0 = float(sys.argv[2])
except IndexError:
    print 'Please provide t, v0 as numeric arguments on the command line, or type them in below'
    t =  float(raw_input('t=? '))
    v0 = float(raw_input('v0=? '))
except:
    print 'Error. Usage: '
    print '$ python ', sys.argv[0], 't v0'
    print 'where t and v0 are numbers'
    sys.exit(1)

g = 9.81
t_low = 0
t_high = 2 * v0 / g

if t < t_low:
    print 't must be 0 or above'
    sys.exit(1)
elif t > t_high:
    print 'With a v0 of', v0, ' the t value must be lower than', t_high
    sys.exit(1)
else:
    y = v0*t - 0.5*g*t**2
    print y


"""
$ python 4.09_ball_cml_errorcheck.py -1 6
t must be 0 or above
"""

"""
$ python 4.09_ball_cml_errorcheck.py 1 6
1.095
"""

"""
$ python 4.09_ball_cml_errorcheck.py 2 6
With a v0 of 6.0  the t value must be lower than 1.22324159021
"""
