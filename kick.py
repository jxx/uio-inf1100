from math import pi

velocities = [120, 10]             # input velocities, km/h
drag_coeff = 0.2                   # Drag coefficient, dimesionless
rho = 1.2                          # Density of air, kg/m^3
ball_radius = .11                  # m
ball_area =  pi * ball_radius ** 2 # m^2
ball_mass = 0.43                   # kg
g = 9.81                           # Gravitational constant, m/s^2
gravity_force = ball_mass * g      # N
kmh_to_ms_factor = 1000./3600.     # Dimensionless

# Calculate drag_force and print output.
# Exercise says to list forces using 1 decimal place;
# however this rounds to drag force = 0.0 for velocity = 10 km/h,
# so 2 decimals has been used for all forces to consistently show

for v in velocities:
    velocity = v * kmh_to_ms_factor 
    drag_force = 0.5 * drag_coeff * rho * ball_area * velocity**2
    force_ratio = drag_force / gravity_force

    print """
    For a ball with mass = %.2f kg and velocity = %.1f m/s, 
    the ball experiences a drag force of %.2f N, 
    the gravity force is %.2f N,
    and the drag:gravity ratio is %.3f
    """ % (ball_mass, velocity, drag_force, gravity_force, force_ratio)

"""
Run output: ~/uio-inf1100$ python kick.py

    For a ball with mass = 0.43 kg and velocity = 33.3 m/s, 
    the ball experiences a drag force of 5.07 N, 
    the gravity force is 4.22 N,
    and the drag:gravity ratio is 1.202
    

    For a ball with mass = 0.43 kg and velocity = 2.8 m/s, 
    the ball experiences a drag force of 0.04 N, 
    the gravity force is 4.22 N,
    and the drag:gravity ratio is 0.008

"""
