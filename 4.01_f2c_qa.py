"""
Make a program that (i) asks the user for a temperature in Fahren-
heit degrees and reads the number; (ii) computes the corresponding
temperature in Celsius degrees; and (iii) prints out the temperature in
the Celsius scale.
"""

def f2c(F):
    C =  (5.0 / 9) * (F - 32)
    return C

F = raw_input('F=? ')
F = float(F)

C = f2c(F)

print C



