"""
Make a table of function values. 
Write a program that prints a table with 
t values in the first columnn and the corresponding 
y(t) = v0 * t - 0.5 * g * t ** 2 values in the second column
"""
t_values = []
y_t_values = []

# Set v0 = 1, g = 9.81, and n = 11
v0 = 1.
g = 9.81
n = 11

# Use n uniformly spaced t values throughout the interval [0, 2v0/g]

for i in range(n+1):
    t_step = 2 * v0 / g
    t = (i + 1) * t_step
    y_t = v0 * t - 0.5 * g * t ** 2
    
    t_values.append(t)
    y_t_values.append(y_t)

    print '%.3f %.3f' % (t_values[i], y_t_values[i])

#print table
