"""
Write a program that prints out a table with Fahrenheit degrees
0, 10, 20, . . . , 100 in the first column and the corresponding Celsius de-
grees in the second column. Hint: Modify the c2f_table_while.py pro-
gram from Chapter 2.1.2. Name of program file: f2c_table_while.py.
"""

temp_table = []

F = 0                          # start value for F
dF = 10                        # increment of F in loop
while F <= 100:                 # loop heading with condition
    C = (5.0/9)*F - 32         # 1st statement inside loop
    temp_table.append(F, C)

print temp_table


