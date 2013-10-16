"""Takes a polynomial as a dictionary p and differenitates it.
This is a dictionary 'killer example' and may very well be on the exam.
"""

# Example: 2 + x**20
# Dictionary represenatation: p = {0: c_0, 20: c_20}
# 
# Here: p = {0: 2, 20: 1}
# In math, to sum: (p[j]*x**j for j in p)
# Exercise 6.16 involves summing of polynomials.

# Alternative representation: p = {'c_0': 2, 'c_20': -1}
# Requires a fix: j = int(j[2:]) to get the coefficients.


def diff(p):
    dp = {}
    for j in p:
        if j != 0: #j0 must be excluded
            dp[j-1] = j*p[j]
    return dp

p = {0: 2, 20: -1} #   2 - x**20
print diff(p)      # -20 * x**19

# x**2 + 2*x + 1
p = {2: 1, 2: 0, 0: 1}
print diff(p)

# x**2 + 2*x + x**10
p = {2: 1, 1: 2, 10: 1}
print diff(p)

# 1000*x + 300*x*4
p = {1: 1000, 4: 300}
print diff(p)
