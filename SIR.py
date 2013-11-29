""" Runs and tests SIR model """

#  Assume ODESolver.py in same folder
from ODESolver import ForwardEuler         # Use FE just to be different...
import numpy as np
from scitools.std import plot 

class RHS:
    """ Returns the right hand sides of the equations for u'=f(u,t)."""
    def __init__(self, v, dt, T, beta):
        # Store parameters in the model
        self.v, self.dt, self.T, self.beta = v, dt, T, beta
    def __call__(self, u, t):

        S, I, R = u                        # Let S, I, R be 3 functions (u)
         
                                           # Change in..
        return [-self.beta*S*I,            # ..suspectible 
                 self.beta*S*I- self.v*I,  # ..infected
                 self.v*I]                 # ..resistant
                                           # persons per dt

def test(b):
    """ Runs test on SIR model, with variying beta """ 

    beta = b #0.0005 or 0.0001             # Infection rate
    v = 0.1                                # Prob. of recovery per dt
    S0 = 1500                              # Init. No. of suspectibles
    I0 = 1                                 # Init. No. of infected
    R0 = 0.                                # Init. No. of resistant 
    U0 = [S0, I0, R0]                      # Initial conditions
    T = 60                                 # Duration, days
    dt = 0.5                               # Time step length in days
    n = T/dt                               # No. of solve steps
    f = RHS(v, dt, T, beta)                # Get right hand side of equation
    solver = ForwardEuler(f)               # Select ODE solver method
    solver.set_initial_condition(U0)
    time_points = np.linspace(0, 60, n+1)
    u, t = solver.solve(time_points)
    S = u[:,0]                             # S is all data in array no 0
    I = u[:,1]                             # I is all data in array no 1
    R = u[:,2]                             # R is all data in array no 2
     

    plot(t, S, t, I, t, R,
         xlabel='Days', ylabel='Persons', 
         legend=['Suspectibles', 'Infected', 'Resistant'],
         hold=('on'))

if __name__ == '__main__':
    test(0.0005)

    """ 
    Manual testing and looking at the graphs shows that over a 60
    day period, a reduction in infection rate from 0.0005 to 0.0001
    will kill the epedemic growth. 

    Thresholds are sensitive, though: 0.0002 and the game is back on. 
    """
    
    

