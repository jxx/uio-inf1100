from math import pi

drag_coeff = 0.2 # Drag coefficient, dimesionless
rho = 1.2 # Density of air, kg/m^3
ball_radius = .11 # m
A =  pi * ball_radius**2 # Area of ball, m^2
ball_mass = 0.43 # kg
g = 9.81 # Gravitational constant, m/s^2
gravity_force = ball_mass*g # N

V_hard = 120 * 5/18 # Hard kick velocity of ball, km/h converted to m/s
V_soft = 10 * 5/18 # Soft kick velocity of ball, km/h converted to m/s

