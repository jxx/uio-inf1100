"""
Write a program that prints out a table with Fahrenheit degrees
0, 10, 20, . . . , 100 in the first column and the corresponding Celsius de-
grees in the second column. Add third column for approximate C = (F-30)/2.
"""

F_degrees = range(0, 110, 10)  
C_degrees = [(5.0 / 9) * (F - 32) for F in F_degrees]
C_approx = [(F - 30) / 2 for F in F_degrees]

Temperature_table = [[F, C, C_approx] for F, C, C_approx in zip(F_degrees, C_degrees, C_approx)]

for F, C, C_approx in Temperature_table:
    print '%8.2f %8.2f %5.0f' % (F, C, C_approx)

"""
$ python 2.2_f2c_approx_table.py 
    0.00   -17.78   -15
   10.00   -12.22   -10
   20.00    -6.67    -5
   30.00    -1.11     0
   40.00     4.44     5
   50.00    10.00    10
   60.00    15.56    15
   70.00    21.11    20
   80.00    26.67    25
   90.00    32.22    30
  100.00    37.78    35
"""
