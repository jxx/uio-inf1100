""" Reads file with GPS coordinates. 
First line contains s, then x,y pairs. 
s = time between readings, in seconds.
The positions are stored as (x, y) coordinates in a file
src/files/pos.dat with the an x and y number on each line, except
for the first line which contains the value of s.
"""
from scitools.std import *

def saveplotpng(filename):
    savefig(filename + '.png')
    print 'Plot saved as ' + filename + '.png'

file  = 'src/files/pos.dat' 
infile = open(file,'r')

# Load s into a float variable and the x and y numbers into two arrays
s = float(infile.readline())

x = []
y = []
for line in infile:
    numbers = line.split()
    x.append(float(numbers[0]))
    y.append(float(numbers[1]))
x_array = array(x)
y_array = array(y)
infile.close


# Plot the y coordinates versus the x coordinates
plot(x_array, y_array, xlabel='x', ylabel='y',
     title='x vs y')
saveplotpng('6.07_x_vs_y')

""" Compute and plot the velocity of the movements."""
# Compute arrays vx and vy with velocities
# Calculated for t = 0..N-2
# t has suffix _curr
# t+1 has suffix _next

N = len(x_array)
index_set = range(N)

# Empty lists for velocities
vx_list = []
vy_list = []

# Velocity is calculated forward, get first values for t=0
t=0
x_curr = x_array[t]
y_curr = y_array[t]

# Continue from t=1:
for t in index_set[1:]:
    x_next = x_array[t]
    y_next = y_array[t]
 
    vx_list.append( (x_next - x_curr) / s )
    vy_list.append( (y_next - y_curr) / s )
    x_curr = x_next
    y_curr = y_next

vx = array(vx_list)
vy = array(vy_list)

# Create set of seconds to use on x axis.
t_values = linspace(0,(N-2)*s,N-1)

# Plot velocities
plot(t_values,vx,t_values,vy,
     xlabel='time (s)', y_label = 'Velocity',
     legend=('X velocity', 'Y velocity'),
     title='Velocities')
saveplotpng('6.07_velocity')

"""
$ python 6.07_position2velocity.py 
Plot saved as 6.07_x_vs_y.png
Plot saved as 6.07_velocity.png
"""
