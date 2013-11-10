"""
Exercise 8.6: Estimate the probability in a dice game.

Estimates the probability of getting at least one of a selected number
when throwing n dice. Runs a number of experiments and compares vs a known exact result.

Command line arguments:

--n    Number of dice to roll                             Default = 1
--N    Number of experiments to run                       Default = 1
--num  Which number of eyes on the dice to look for       Default = 6
--res  Exact result to compare against, between 0 and 1   Default = float(1)/6
"""

import sys
import numpy as np
import argparse

def roll_dice_get_at_least_one_of(number, n):
    """ Returns true if at least one of the number shows up on n dice rolls"""
    eyes = np.random.randint(1, 7, n)

    # Create True/False array of number of successes
    success = eyes == number    
    
    # Sum number of successes
    M = np.sum(success)

    # If more than one dice has the correct number of eyes, return True
    if M > 0:
        return True

def run_experiments(N, n):
    """ Returns the fraction of dice rolls that are considered a success"""
    M = 0
    for i in xrange(N):
        outcome = roll_dice_get_at_least_one_of(6, n)
        if outcome:
            M += 1
    return float(M)/N

def vectorized_experiment(N, ndice, nsix):

    eyes = np.random.random_integers(1, 6, (N, ndice))
    compare = eyes == 6
    nthrows_with_6 = np.sum(compare, axis=1)  # sum over columns
    nsuccesses = nthrows_with_6 >= nsix
    M = np.sum(nsuccesses)
    p = float(M)/N
    print 'probability:', p
    return p


parser = argparse.ArgumentParser()
parser.add_argument('--ndice', '--numberofdice', type=int,
                    default=1, help='Number of dice to roll')
parser.add_argument('--N', '--numberofexperiments', type=int,
                    default=1, help='Number of experiments to run')
parser.add_argument('--num', '--number', type=int,
                    default=6, help='Which eye on dice to look for')
parser.add_argument('--res', '--result', type=float,
                    default=float(1)/6, help='Exact known probability')
parser.add_argument('--nsix', '--numberofsixes', type=float,
                    default=2, help='Desired number of sixes')
args = parser.parse_args()

ndice = args.ndice
N = args.N
number = args.num
nsix = args.nsix
exact_result = args.res

print """Running Experiment """
print ndice, " dice, ",  N, " experiments"
estimated_result = run_experiments(N, ndice)
estimated_result2 = vectorized_experiment(N, ndice, 1) 
print "Estimated result: %.8f, %.8f difference from exact result" % \
(estimated_result, estimated_result-exact_result)
print estimated_result2

"""
 $ python 8.06_one6_ndice.py --n 2 --N 10000 --res 0.305555555
Running Experiment 
2  dice,  10000  experiments
Estimated result: 0.30720000, 0.00164444 difference from exact result
"""

