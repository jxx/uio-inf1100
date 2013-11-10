"""
Exercise 8.2: Compute probabilities

What is the probability of getting a number between 0.5 and 0.6
when drawing uniformly distributed random numbers from the interval
[0, 1)? To answer this question empirically, let a program draw N such
random numbers using Python's standard random module, count how
many of them, M , that fall in the interval (0.5, 0.6), and compute the
probability as M/N . Run the program with the four values N = 10i
for i = 1, 2, 3, 6. Name of program file: compute_prob.py.
"""

def draw_random_uniform(N):
    import random                      # Use Python's standard random module.
    M, p = 0, 0                        # Assign intitial variable values.
    for e in range(N):                 # Draw N
        r = random.uniform(0, 1)       # random numbers in range [a, b).
        if r > 0.5 and r < 0.6:        # If in interval (0.5, 0.6) then
            M += 1                     # count M and
            p = float(M)/N             # compute probability

    return p 

# Test cases
if __name__ == '__main__':
    print """
    Probabilities for drawing a number between 0.5 and 0.6.
    N draws, N=10**i for i = 1, 2, 3, 6
    """

    for i in [1, 2, 3, 6]:             # Run the program with 4 values,
        P = draw_random_uniform(10**i) # N=10**i for i = 1, 2, 3, 6
 
        print 'For N=%g P=%.6f' % (10**i, P)

"""
$ python 8.02_compute_prob.py 

    Probabilities for drawing a number between 0.5 and 0.6.
    N draws, N=10**i for i = 1, 2, 3, 6
    
For N=10 P=0.100000
For N=100 P=0.090000
For N=1000 P=0.091000
For N=1e+06 P=0.099757
"""
