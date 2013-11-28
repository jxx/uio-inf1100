import ODESolver
from scitools.std import plot
import numpy as np

class Problem:
   
    def __init__(self, nu, beta, S0, I0, R0, T):
        """
        Creates an instance of a set of infection ODEs
  
        nu, beta: parameters in the ODE system
        S0, I0, R0: initial values
        T: simulation for t in [0,T]
        """

        self.beta = beta
        self.nu = nu

        # Wrap nu as function
        if isinstance(nu, (float,int)):     # number?
            self.nu = lambda t: nu          # wrap as function
        elif callable(nu):
            self.nu = nu

        # Wrap beta as function
        if isinstance(beta, (float,int)):   # number?
            self.beta = lambda t: beta      # wrap as function
        elif callable(beta):
            self.beta = beta      

        # Store the other parameters
        self.S0, self.I0, self.R0 = S0, I0, R0 
        self.T = T

    def __call__(self, u, t):
        # Let S, I, R be 3 ODEs u and return RHS
        S, I, R = u                              
        
        # Representing change in..
        return [-self.beta(t) * S * I,      # ..suspectible 
                 self.beta(t) * S * I
                 -self.nu(t) * I,           # ..infected
                 self.nu(t) * I]            # ..resistant
        # persons per dt


class Solver:
    """ Uses methods from ODESolver to solve the ODEs """
    def __init__(self, problem, dt):
        # Creates an instance of a Solver object for the problem

        self.problem, self.dt = problem, dt

    def solve(self, method=ODESolver.RungeKutta4):
        # Solves the ODE using ODESolver

        # Create ODESolver instance of problem using chosen method
        self.solver = method(self.problem)

        # List and set of intitial conditions
        ic = [self.problem.S0, self.problem.I0, self.problem.R0]
        self.solver.set_initial_condition(ic)

        # Prepare time array
        n = int(round(self.problem.T/float(self.dt)))
        t = np.linspace(0, self.problem.T, n+1)

        # Solve for t with a little help from ODESolver
        u, self.t = self.solver.solve(t)
        self.S, self.I, self.R = u[:,0], u[:,1], u[:,2]

    def plot(self):
        # Plots S(t), I(t), and R(t) vs T

        plot(self.t, self.S, self.t, self.I, self.t, self.R,
             xlabel='Days', ylabel='Persons', 
             legend=['Suspectibles', 'Infected', 'Resistant'])

    def getmax(self):
        return max(self.I)


def test():
    
    # nu = recovery chance per dt. Can be a function.
    # S0 = initial healthy population
    # I0 = infected persons at simulation start
    # T  = duration (here: days)
    # beta = infection chance per SI pair. Can be a function.

    # Create instance of class Problem using lambda construction for beta.
    problem = Problem(beta=lambda t: 0.0005 if t <= 12 else 0.0001,
                      nu=0.1, S0=1500,      # Keep nu constant
                      I0=1, R0=0, T=60)     # Calls problem.__init__

    # Lambda function is equivalent of
    """
    def mybeta(t):
    if t <= 12:
        return 0.0005
    else:
        return 0.0001
    """

    # Send problem instance to solver, using dt = 0.5
    # This creates a solver instance that can solve and plot
    solver = Solver(problem, 0.5)           # Calls solver.__init__

    solver.solve()
    # solver.plot()
    print "The maximum number of infected people is", \
    int(round(solver.getmax()))

    # Redo previous scenario where beta is constant
    problem =  Problem(beta=0.0005, 
                       nu=0.1, S0=1500,     
                       I0=1, R0=0, T=60)    
    solver = Solver(problem, 0.5)         
    solver.solve()
    
    print "compared to %g for b=0.0005" %  int(round(solver.getmax())) 
    
if __name__ == '__main__':
    test()

"""
$ python SIR_class.py 
The maximum number of infected people is 745
compared to 897 for b=0.0005
"""
