from scitools.std import *

v0 = 10
g = 9.81

n = 501
t = linspace(0, 2*v0/g, n)
y = v0*t - 0.5*g*t**2

plot(t, y)
xlabel('time (s)')
ylabel('height (m)')
title('My first plot')
savefig('ball_plot.png')

# Alternative 1: sleep/pause
import time
time.sleep(2)  # 2 sec pause

# Alternative 2: let the program hang
raw_input()  # make plot stay on the screen
