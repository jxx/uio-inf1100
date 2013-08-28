from math import pi

Velocities = [120, 10] # input velocities, km/h

drag_coeff = 0.2 # Drag coefficient, dimesionless
rho = 1.2 # Density of air, kg/m^3
ball_radius = .11 # m
ball_area =  pi * ball_radius**2 # Area of ball, m^2
ball_mass = 0.43 # kg
g = 9.81 # Gravitational constant, m/s^2
gravity_force = ball_mass*g # N
kmh_to_ms_factor = 1000./3600.


for V in Velocities:
    Velocity = V * kmh_to_ms_factor 
    drag_force = 0.5 * drag_coeff * rho * ball_area * Velocity
    print drag_force
