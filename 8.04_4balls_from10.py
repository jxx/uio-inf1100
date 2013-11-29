"""
40 balls in a hat, 10 red, 10 blue, 10 yellow, 10 purple.
What is the prob of drawing 2 blue, 2 purple when drawing 10 balls at random.
"""
print 'Exercise 8.4'

import random
import sys

def new_hat():
    hat = []
    for i in range(10):
        hat.append('blue')
        hat.append('red')
        hat.append('yellow')
        hat.append('purple')

    return hat


def do_experiment():
    hat = new_hat()
    drawn = []

    for i in range(10):
        ball = random.randint(0,len(hat)-1)

        # removes random element and appends to new list
        drawn.append(hat.pop(ball)) 

    return drawn.count('blue') == 2 and drawn.count('purple') == 2


num_experiments = int(sys.argv[1])
num_successes = 0

for i in range(num_experiments):
    if do_experiment():
        num_successes += 1

print num_successes/float(num_experiments)
    
