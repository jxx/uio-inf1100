"""
Exercise E.27. Implement the iterated Midpoint method; class.
The purpose of this exercise is to implement the numerical
method (E.46)–(E.47) in a class like the ForwardEuler class from
Appendix E.1.7. Create a module containing the class and a test
function demonstrating the use:

def _application():
    def f(u, t):
        return -2*u
    solver = MidpointIter(f, N=4)
    solver.set_initial_condition(1)
    t_points = numpy.linspace(0, 1.5, 16)
    u, t = solver.solve(t_points)
    from scitools.std import plot
    plot(t, u)

Call the _application function from the test block in the module file.
Also include a _verify function which compares the hand calculations
of two time steps (see Exercise E.26) with the results produced by the
class. Name of program file: MidpointIter_class.py.
"""
