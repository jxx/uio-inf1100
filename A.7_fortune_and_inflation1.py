from scitools.std import *
import argparse
import sys
import pprint

def net_fortune(N, x0, c0, p=0.0, I=0.0):
    """ 
    Computes net fortune after 
    N  -- Years 
    x0 -- Initial fortune
    c0 -- Yearly initial consumption
    p  -- Yearly interest rate from fortune, in decimals
    I  -- Yearly inflation, in decimals.

    Returns a tuple of three arrays: 
    Year number
    Net fortune per year, adjusted for inflation
    Consumption per year, adjusted for inflation
    """

    index_set =  range(N+1)
    x = zeros(len(index_set))
    c = zeros(len(index_set))
    x[0] = float(x0)
    c[0] = float(c0)
 
    for n in index_set[1:]:
        x[n] = x[n-1] + p * x[n-1] - c[n-1]
        c[n] = c[n-1] + I * c[n-1]
        
    #plot(index_set, x, 'r', xlabel='Years', ylabel='Net Fortune')

    return array(index_set), x, c

# Parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('N', type=int, 
                    help = 'Number of years')
parser.add_argument('x0', type=float, 
                    help = 'Initial fortune')
parser.add_argument('c0', type=float, 
                    help = 'Initial yearly consumption')
parser.add_argument('p', type=float, 
                    help = 'Yearly interest rate from fortune, in decimals')
parser.add_argument('I', type = float,
                    help = 'Yearly inflation, in decimals.')

args = parser.parse_args()

# Call 
x = net_fortune(args.N, args.x0, args.c0, args.p, args.I)
pprint.pprint(x)

plot(x[0], # First array is Years
     x[1], # Second array is Net fortune
     'r', 
     xlabel='Years', 
     ylabel='Net Fortune')

savefile = sys.argv[0] + '.png'
savefig(savefile)
print 'Plot saved as', savefile

"""
$ python A.7_fortune_and_inflation1.py 10 1000 40 .05 .02
(array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10]),
 array([ 1000.        ,  1010.        ,  1019.7       ,  1029.069     ,
        1038.07413   ,  1046.6805501 ,  1054.85134548,  1062.54741598,
        1069.72736007,  1076.34735284,  1082.36101773]),
 array([ 40.        ,  40.8       ,  41.616     ,  42.44832   ,
        43.2972864 ,  44.16323213,  45.04649677,  45.94742671,
        46.86637524,  47.80370274,  48.7597768 ]))
Plot saved as A.7_fortune_and_inflation1.py.png
"""
