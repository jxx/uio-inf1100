from math import asin

h = 0.01
x = [i * h for i in range(0, 101, 1)]

y = []

for x_i in x:
    y.append(asin(x_i))

print x
print y

for x_i, y_i in zip(x, y) : # zip takes two or more LISTS as args 
    print '%.3f %.3f' % (x_i, y_i) # uses same index for all lists per iteration

""" 
#same same but longer:
for i in range(len(x)):
    x_i = x[i]
    x_y = y[i]
    print  '%.3f %.3f' % (x_i, y_i) 
"""
