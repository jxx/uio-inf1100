"""
After having computed the two lists of t and y values in the program from 
Exercise 2.7, store the two lists in a new list ty1. Write out a table
of t and y values by traversing the data in the ty1 list. Thereafter, make a 
list ty2 which holds each row in the table of t and y values. Write out the 
table by traversing the ty2 list.
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

# ty1 is a list of table columns:
ty1 = [t_values, y_values]
print '\n' + "   Traversing ty1:"

for i in range(len(t_values)):
    for j in range(len(ty1)):
        value = ty1[j][i]
        print '%8.3f' % value,
    print

#ty2 is a list of table rows:
ty2 = []
for t_value, y_value in zip(t_values, y_values):
    ty2.append([t_value, y_value])

print '\n' + "   Traversing ty2:"
for t_value, y_value in ty2:
    print '%8.3f %8.3f' % (t_value, y_value)


"""
$ python 2.19_ball_table3.py 

   Traversing ty1:
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

   Traversing ty2:
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
