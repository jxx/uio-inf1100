"""
Exercise 8.6: Estimate the probability in a dice game.

Estimates the probability of getting at least one of a selected number
when throwing n dice. Runs a number of experiments and compares vs a known exact result.

Command line arguments:

--ndice Number of dice to roll                             Default = 2
--N     Number of experiments to run                       Default = 1000000
--nsix  Number of 6es we want to see                       Default = 1
--res   Exact result to compare against, between 0 and 1   Default = float(11)/36

Code contains iterated and vectorized version of experiment. Vectorized is used in runtime example.
"""

import sys
import numpy as np
import argparse
import time

def roll_dice_get_at_least_one_of(ndice):
    """ Returns true if at least one 6 shows up on ndice die rolls"""
    eyes = np.random.randint(1, 7, ndice)

    # Create True/False array of number of successes
    success = eyes == 6
    
    # Sum number of successes
    M = np.sum(success)

    # If more than one dice has the correct number of eyes, return True
    if M > 0:
        return True

def run_experiments_iterated(N, ndice):
    """ Returns the fraction of dice rolls that are considered a success"""
    M = 0
    for i in xrange(N):
        outcome = roll_dice_get_at_least_one_of(6, ndice)
        if outcome:
            M += 1
    return float(M)/N

def run_experiment_vectorized(N, ndice, nsix):
    """ Returns the probability of getting nsix 6es when rolling ndice in N experiments """

    # Roll dice
    eyes = np.random.random_integers(1, 6, (N, ndice))

    # Create True/False array of compare values
    compare = eyes == 6

    # Count number of 6es
    nthrows_with_6 = np.sum(compare, axis=1)

    # Create True/False array of successes, sum Trues and calculate probability
    nsuccesses = nthrows_with_6 >= nsix
    M = np.sum(nsuccesses)
    p = float(M)/N
    return p


parser = argparse.ArgumentParser()
parser.add_argument('--ndice', '--numberofdice', type=int,
                    default=2, help='Number of dice to roll')
parser.add_argument('--N', '--numberofexperiments', type=int,
                    default=1000000, help='Number of experiments to run')
parser.add_argument('--res', '--result', type=float,
                    default=float(11)/36, help='Exact known probability')
parser.add_argument('--nsix', '--numberofsixes', type=float,
                    default=1, help='Desired number of sixes')
args = parser.parse_args()

ndice = args.ndice
N = args.N
nsix = args.nsix
exact_result = args.res

print """Running Experiment  """
N, " experiments rolling ", ndice, " dice and getting ", nsix, " or more 6es"
estimated_result = run_experiment_vectorized(N, ndice, nsix) 
print "Estimated result: %.8f, %.8f difference from exact result" % \
(estimated_result, estimated_result-exact_result)

"""
$ python 8.06_one6_ndice.py --ndice 2 --N 100000000
Running Experiment  
Estimated result: 0.30550001, -0.00005555 difference from exact result
"""
