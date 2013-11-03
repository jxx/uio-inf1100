"""
An ordinary differential equation (ODE) written in generic form:

                     u' (t) = f (u(t), t)

The solution of this equation is a function u(t)

To obtain a unique solution u(t), the ODE must have an initial condition:
                           u(0) = U_0

Uses Forward Euler function.

THis function generates a sewuence of u1, u2...., n values for u at times t1, t2, .... n

I.e. a simple-stepping-forward-in-time function

Must know solution for t=0.

Algo:
Create arrays u adn t to hold u_ and t_k for k = 0,1,2,3....n
Set iitial condition u[0] = U_0

u[k+1] = u[k] + dt*f(u[k], t[k])
t[k] = t[k] + dt

"""
