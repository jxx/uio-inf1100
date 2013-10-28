"""
"""
print 'Exercise E.26. Implement the iterated Midpoint method'

from scitools.std import *

def iterated_Midpoint_method(f, U0, T, n, N):
    t = zeros(n+1)
    u = zeros(n+1) # solution ar t[n]
    v = zeros(N+1)
    u[0] = U0
    t[0] = 0
    dt = T/float(n)

    for k in range(n):
        t[k+1] = t[k] + dt
        # Forward Euler
        v[0] = u[k]
    
        for q in range(1, N+1):
        
            v[q] = u[k] + 0.5 * dt * (f(v[q-1], t[k+1]) + f(u[k], t[k]))
        
        u[k+1] = v[N]

    return u, t

def ForwardEuler(f, U0, T, n):
    """Solve u'=f(u,t), u(0)=U0, with n steps until t=T."""
    import numpy as np
    t = np.zeros(n+1)
    u = np.zeros(n+1)  # u[k] is the solution at time t[k]
    u[0] = U0
    t[0] = 0
    dt = T/float(n)
    for k in range(n):
        t[k+1] = t[k] + dt
        u[k+1] = u[k] + dt*f(u[k], t[k])
    return u, t


#""" ForwadEuler Example
def f(u, t):
    # u' = -2u
    return u



u, t = ForwardEuler(f, U0=1, T=3, n=30)

u1, t1 = iterated_Midpoint_method(f, U0=1, T=3, n=30, N=1)

u2, t2 = iterated_Midpoint_method(f, U0=1, T=3, n=30, N=2)

# Compare numerical solution and exact solution in a plot
from scitools.std import plot, exp
u_exact = exp(t)
plot(t, u, 'r-', t, u_exact, 'b-', t, u1, t, u2,
     xlabel='t', ylabel='u', legend=('numerical', 'exact', 'N=1', 'N=2'),
     title="Solution of the ODE u'=u, u(0)=1")

# Verify by hand calculations
u, t = ForwardEuler(f, U0=1, T=0.2, n=2)
print u, [1, 1,1, 1.21]

# Verify by exact numerical solution
def f1(u, t):
    return 0.2 + (u - u_solution_f1(t))**4

def u_solution_f1(t):
    return 0.2*t + 3

u, t = ForwardEuler(f1, U0=3, T=3, n=5)
print 'Numerical:', u
print 'Exact:    ', u_solution_f1(t)

# Accuracy check for decreasing time step (u'=u, u(0)=1)
T = 3; U0 = 1
for dt in 0.5, 0.05, 0.005:
    n = int(round(T/dt))
    u, t = ForwardEuler(f, U0, T, n)
    print 'dt=%.5f, u(%g)=%.6f, error=%g' % \
          (dt, t[-1], u[-1], exp(t[-1]-u[-1]))
    

# E26 test case

def f(u, t):
    # u' = -2u
    return u

#u_Exact = exp(-2*t)


U0 = 1
T = 2
dt = 0.1
# n*dt = T
n = int(T/dt) # int(round(T/dt)) math rounding

u,t = iterated_Midpoint_method(f, U0=U0, T=T, n=n, N=2)

print u, t

