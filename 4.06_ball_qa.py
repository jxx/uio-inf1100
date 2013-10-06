"""
Get user input for t and v0 instead of the following line:
v0 = 3; g = 9.81; t = 0.6
"""
t = raw_input('t=? ')
v0 = raw_input('v0=? ')

t = float(t)
v0 = float(v0) 

g = 9.81

y = v0*t - 0.5*g*t**2
print y


"""
$ python 4.06_ball_qa.py 
t=? 1
v0=? 6
1.095
"""
