import numpy as np
import scitools as sci

f = open('examples/files/xy.dat', 'r')

x = []
y = []

for line in f:
    splitted = line.split()
    x.append(float(splitted[0]))
    y.append(float(splitted[0]))

x_array = np.array(x)
y_array = np.array(y)

print 'Min y = %f, max y = %f' % (min(y), max(y))

sci.std.plot(x_array, y_array)
