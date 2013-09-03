"""
Make a table of function values. 
Write a program that prints a table with 
t values in the first columnn and the corresponding 
y(t) = v0 * t - 0.5 * g * t ** 2 values in the second column
"""

t_values = []
y_values = []

# Set v0 = 1, g = 9.81, and n = 11
v0 = 1.
g = 9.81
n = 11

for i in range(n+1):
    
    # Use n uniformly spaced t values throughout the interval [0, 2v0/g] 
    t_step = 2 * v0 / g
    t = (i + 1) * t_step
    y_t = v0 * t - 0.5 * g * t ** 2

    # so that the t and y values are stored in two lists t and y.    
    t_values.append(t)
    y_values.append(y_t)

    #print '%.3f %.3f' % (t_values[i], y_values[i])

# Thereafter, transverse the lists with a for loop and write out
# a nicely formatted table of t and y values 
# (using either a zip or range construction).
for t_value, y_value in zip(t_values, y_values):
    print '%8.3f %8.3f' % (t_value, y_value)
