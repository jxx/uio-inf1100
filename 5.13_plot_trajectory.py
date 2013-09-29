from scitools.std import *

def yfunc(t):
    return v0*t - 0.5*g*t**2

g = 9.81

if len(sys.argv) == 1:
    print 'Give v0 values on the command line!'
    sys.exit(1)
    
for v0_str in sys.argv[1:]:
    v0 = float(v0_str)
    t = linspace(0, 2*v0/g, 101)
    y = yfunc(t)
    plot(t, y)
    hold('on')
    legend('v0=%g' % v0)  # mark this line

xlabel('time')
ylabel('height')
