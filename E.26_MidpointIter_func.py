"""
Exercise E.26. Implement the iterated Midpoint method; function.
Implement the numerical method (E.46)–(E.47) as a function
iterated_Midpoint_method(f, U0, T, n, N)
where f is a Python implementation of f (u, t), U0 is the initial condi-
tion u(0) = U0 , T is the final time of the simulation, n is the number
of time steps, and N is the parameter N in the method (E.46). The
iterated_Midpoint_method should return two arrays: u0 , . . . , un and
t0 , . . . , tn . To verify the implementation, calculate by hand u1 and u2
when N = 2 for the ODE u' = −2u, u(0) = 1, with ∆t = 1/4. Compare
your hand calculations with the results of the program. Thereafter, run
the program for the same ODE problem but with ∆t = 0.1 and T = 2.
Name of program file: MidpointIter_func.py.
"""
