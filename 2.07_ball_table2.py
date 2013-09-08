"""
Make a table of function values. Write a program that prints a table with 
t values in the first columnn and the corresponding 
y(t) = v0 * t - 0.5 * g * t ** 2 values in the second column
"""

t_values = []
y_values = []

# Set v0 = 1, g = 9.81, and n = 11
v0 = 1
g = 9.81
n = 11
tolerance = 1E-14 # fudge since float operator is not precise

# compute t values
dt = (2 * v0/g - 0)/(n-1) # spacing of t values
t = 0

while t <= 2 * v0 / g + tolerance:
    t_values.append(t)
    t = t + dt

# Using list comprehension for y_values:
y_values = [v0 * t - 0.5 * g * t ** 2 for t in t_values]

"""
Thereafter, transverse the lists with a for loop and write out a nicely 
formatted table of t and y values (using either a zip or range construction).
"""

for t_value, y_value in zip(t_values, y_values):
    print '%8.3f %8.3f' % (t_value, y_value)

"""
uio-inf1100$ python 2.7_ball_table2.py 
   0.000    0.000
   0.020    0.018
   0.041    0.033
   0.061    0.043
   0.082    0.049
   0.102    0.051
   0.122    0.049
   0.143    0.043
   0.163    0.033
   0.183    0.018
   0.204   -0.000
"""
