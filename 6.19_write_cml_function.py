"""
Reads a function from the command line and writes x and f (x) values to a file,
where the x values appear in the first column and the f (x) values appear in the second.

Provide command line args as follows:

--f    The function to be evaluated, like 'sin(x)'       Default = None
--a    Lower bound of x.                                 Default = 0.0
--b    Upper bound of x (up to and including b).         Default = 1.0
--n    number of x values in the interval a,b            Default = 11
--o    Output filename                                   Default = 'list.txt'

"""

# We want to be able to process a number of different equations so we import all of scitools.std
from scitools.std import *

# Set up command line argument parsing
import argparse
parser = argparse.ArgumentParser()


parser.add_argument('--f', '--function', type=str,
                    default='', help='Function f(x) x as text')
parser.add_argument('--a', '--from', type=float,
                    default=0.0, help='Lower bound')
parser.add_argument('--b', '--to', type=float,
                    default=10.0, help='Upper bound')
parser.add_argument('--n', '--noofvals', type=int,
                    default=11.0, help='Number of values between lower and upper bounds')
parser.add_argument('--o', '--output', type=str,
                    default='list.txt', help='Output filename')

args = parser.parse_args()

# Assign arguments to variables
try:
    f = StringFunction(args.f)
except:
    print 'You must provide a valid function sting in the format f(string) where x is the variable'
    sys.exit(1)

a = args.a
b = args.b
n = args.n
filename = args.o
outfile = open(filename,'w')


# Create array of x values from a to b in n steps:
x_values = linspace(a, b, n)

# Indices to traverse x
index_set = range(len(x_values))

# Create array of zeros for y values:
y_values = zeros(len(x_values))

# Assign f(x) values for each x value
for i in index_set:
    y_values[i] = f(x_values[i])

# Combine into one table
table = zip(x_values, y_values)

# Traverse table and print data points to file. 
for row in table:
    for column in row:
        outfile.write('%14.8f' % column)
    outfile.write('\n')
outfile.close

print 'Data for f(x) = ' + str(f) + ' for ' + str(n) + ' x points from ' + str(a) + ' to ' + str(b) + ' has been written to ' + filename

"""
$ python 6.19_write_cml_function.py --f 'x*(12-x)+sin(pi*x)' --b 10 --n 101
Data for f(x) = x*(12-x)+sin(pi*x) for 101 x points from 0.0 to 10.0 has been written to list.txt
"""
