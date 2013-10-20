"""
Reads file with a x,y coordinate pair per line
First line contains s, then x,y pairs.
s = time between readings, in seconds.
"""
from scitools.std import *
file  = 'examples/files/pos.dat'

infile = open(file,'r')
s = float(infile.readline())

# Set up empty lists
x = []
y = []
vx = []
vy = []


for line in infile:
    numbers = line.split()
    x.append(float(numbers[0]))
    y.append(float(numbers[1]))

x_array = array(x)
y_array = array(y)
infile.close

# Velocity for time t is calculated using current t and t+1. 
# We get the first values as current

n=0
x_curr = x_array[n]
y_curr = y_array[n]

sint = int(s)
print type(sint)

index_set = range(len(x_array+1))
plot_set = range(0,(len(x_array)-1)*sint,sint)

#plot_set = linspace(0,(len(x_array-1)*s,s))

print plot_set

#while n <= len(x_array)-1:
for n in index_set[1:]:
    x_next = x_array[n]
    y_next = y_array[n]
 
    vx.append( (x_next - x_curr) / s )
    vy.append( (y_next - y_curr) / s )
    x_curr = x_next
    y_curr = y_next

#    n += 1
    
#plot(x_array, y_array)

vx_array = array(vx)
vy_array = array(vy)

print vx_array
print vy_array

plot(plot_set,vx_array,plot_set,vy_array)
