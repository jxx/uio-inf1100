"""
Exercise 4.8. Make the program from Exer. 4.7 safer.
The program from Exercise 4.7 reads input from the command
line. Extend that program with exception handling such that miss-
ing command-line arguments are detected. In the except IndexError
block, use the raw_input function to ask the user for missing input
data. Name of program file: ball_cml_qa.py.
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

y = v0*t - 0.5*g*t**2
print y

"""
$ python 4.08_ball_cml.qa.py 1 6
1.095
"""

"""
$ python 4.08_ball_cml.qa.py 
Please provide t, v0 as numeric arguments on the command line, or type them in below
t=? 1
v0=? 6
1.095
"""

"""
$ python 4.08_ball_cml.qa.py a b
Error. Usage: 
$ python  4.08_ball_cml.qa.py t v0
where t and v0 are numbers
"""
