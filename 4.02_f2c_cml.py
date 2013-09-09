"""
Make a program that (i) asks the user for a temperature in Fahren-
heit degrees and reads the number; (ii) computes the corresponding
temperature in Celsius degrees; and (iii) prints out the temperature in
the Celsius scale.
"""

def f2c(F):
    C =  (5.0 / 9) * (F - 32)
    return C

import sys

#F = raw_input('F=? ')

F = float(sys.argv[1])

C = f2c(F)

print C



