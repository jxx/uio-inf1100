#class notes: lists
#known objects: float, int, str, bool
#new object: list
#list: collection of objects with a sequence
"""
C = [-20, -15, -5, 0, 5]
filename = ['myprog.py', 'odd.py']

b= 3 > 4
another_list = [2, 3.4, 'a string', b]

print another_list

print C

print C[0] #1st element
print C[-1] #last element


#sublist
sublist_of_C = C[1:3] # from 1 up to bit not including 3

print sublist_of_C
print 'end 1'

#add an element

C.append(50)
print C
"""
#for loops
#this code can be simplified:
C_degrees = [10,20,30]
F_degrees = []

for C in C_degrees:
    F = 9./5*C + 32
    F = F_degrees.append(F)
print F_degrees

# compact for: list comprehension
F_degrees = [9./5*C + 32 for C in C_degrees]
print F_degrees

#range: generates a list of integers
integers = range(2, 14, 2) # (start, uptobutnotincluding, step)
print integers
for i in range(0,len(C_degrees),1):
    print C_degrees[i]

#short form. start defaults to 0 and step to 1: 
for i in range(len(C_degrees)):
    print C_degrees[i]

#list comprehension 2:
n=6
odd_numbers = [i for i in range (1, n+1, 2)] #list. i is both index and output

# short form
odd_numbers = range(1, n+1, 2)


#compute t values in [0, 2*v0/g]
v0 =1
g = 9.81
n = 11

t_values= []
dt = (2 * v0 / g - 0)/float(n-1) #floar unnecessary as g is a float and forces function data type to be float
t=0
while t <= 2 * v0/g:
    t_values.append(t)
    t = t + dt #why is dt the formula above?
#list comprehension
y = [v0*t - 0.5*g*t**2 for t in t_values] #note and understand t in t_values

#alternative: full for loop

y=[]
for t in t_values:
    formula = v0 * t - 0.5*g*t**2
    y.append(formula)

#loop through two lists with index:
for i in range(len(t_values)):
    print '%8.3f %8.3f' % (t_values[i], y[i])

# zip takes two or more lists and loops through them in parallell:
for t_value, y_value in zip(t_values, y):
    print '%8.3f %8.3f' % (t_value, y_value)

# Add 5 to all elements in C_degrees
for C in C_degrees:
    C = C + 5
print C_degrees # THIS IS  WRONG. THE C = C + 5 

# Must index the list on the left hand side
for i in range(len(C_degrees)):
    C_degrees[i] = C_degrees[i] + 5
print C_degrees


