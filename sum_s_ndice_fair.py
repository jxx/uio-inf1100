"""
Exercise 8.9: sum s ndice fair

Exercise 8.9. Adjust the game in Exer. 8.8.
It turns out that the game in Exercise 8.8 is not fair, since you lose
money in the long run. The purpose of this exercise is to adjust the
winning award so that the game becomes fair, i.e., that you neither
lose nor win money in the long run.

Make a program that computes the probability p of getting a sum
less than s when rolling n dice. Use the reasoning in Chapter 8.3.2 to
find the award per game, r, that makes the game fair. Run the program
from Exercise 8.8 with this r on the command line and verify that the
game is now fair. Name of program file: sum_s_ndice_fair.py.

"""

from sum9_4dice import *
import numpy as np

def win_probability_iterated(N, ndice):
    M = 0
    for i in range(N):
        under9 = 0
        if  compute_win(ndice, 9):
            M += 1
    return float(M)/N

def win_probability_vectorized(N, n, ndice):
    """ Returns the probability of getting < n when rolling ndice in N experiments """

    # Roll dice
    eyes = np.random.random_integers(1, 6, (N,ndice))
    
    # Create array of compare values
    compare = np.sum(eyes, axis = 1)

    # Create True/False array of successes, sum Trues and calculate probability
    nsuccesses = compare < n
    M = np.sum(nsuccesses)
    p = float(M)/N
    return p

if __name__ == '__main__':
    P = win_probability_vectorized(10000, 9, 4)
    print "Win probability: ", P
    expected_payout = 10 * P - 1
    print "Expected payout per game:", expected_payout

    award = 1 / P + 1 # Returns fair win sum for cost of 1 per game to average 0 returns

    print "Fair payout for a win should be: ", award

    play(10000, 4, 0, award)

""" Two examples, to show that results vary.
$ python sum_s_ndice_fair.py 
Win probability:  0.0556
Expected payout per game: -0.444
Fair payout for a win should be:  18.9856115108
Net result after 10000 rounds: 522 wins, -89 net capital
You should not play this game

$ python sum_s_ndice_fair.py 
Win probability:  0.0535
Expected payout per game: -0.465
Fair payout for a win should be:  19.691588785
Net result after 10000 rounds: 575 wins, 1322 net capital
You could play this game
"""
