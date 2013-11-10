"""
Exercise 8.8: sum 9, 4 dice

Decides if a dice game is fair. 
You pay c euro and are allowed to throw four dice.
If the sum of the eyes on the dice is less than w, you win r euros, otherwise you lose your investment.

Should you play this game when 

w = 9, r = 10, c = 1

Command line arguments:

--r      Get this amount if you win a game     Default = 10
--N      Number of experiments                 Default = 10
--ndice  Number of dice to roll in game        Default = 4
--w      Get less than this sum to win         Default = 9
--c      Cost to play one round                Default = 1
"""

import random
import argparse

global win_count, loss_count  # Nasty global variables

def roll_dice_and_compute_sum(ndice):
    """ Rolls ndice and returns the sum """
    return sum([random.randint(1, 6) \
                for i in range(ndice)])

def compute_win(ndice, win_value):
    """ Checks if rolled sum qualifies as a win """
    computesum = roll_dice_and_compute_sum(ndice)
    if computesum < win_value:
        return True # You win the game

def play_one_round(ndice, capital, win_amount, win_count):
    win =  compute_win(ndice, win_value)
    if win:
        capital += win_amount - play_cost
        win_count += 1
    else:
        capital -= play_cost
    return capital, win_count

def play(nrounds, ndice, win_count, win_amount):
    player_capital = 0 # We are only concerned with net gain in this simulation

    for i in range(nrounds):
        player_capital, win_count = play_one_round(ndice, player_capital, win_amount, win_count)

    print "Net result after %d rounds: %d wins, %d net capital" % \
        (nrounds, win_count, player_capital)

    if player_capital < 0:
        print "You should not play this game"
    else:
        print "You could play this game"

parser = argparse.ArgumentParser()
parser.add_argument('--r', '--return', type=float,
                    default=10, help='Get this amount if you win a game')
parser.add_argument('--N', '--numberofexperiments', type=int,
                    default=10, help='Number of experiments to run')
parser.add_argument('--ndice', '--numberofdice', type=int,
                    default=4, help='Number of dice to roll')
parser.add_argument('--w', '--winvalue', type=int,
                    default=9, help='Get less than this value to win')
parser.add_argument('--c', '--play_cost', type=int,
                    default=1, help='Cost to play one round')


args = parser.parse_args()
win_amount = args.r
N = args.N
ndice = args.ndice
win_value = args.w
play_cost = args.c
win_count = 0

if __name__ == '__main__':

    play(N, ndice, win_count, win_amount)

"""
$ python sum9_4dice.py --N 100
Net result after 100 rounds: 5 wins, -50 net capital
You should not play this game
"""
