from math import log, pi

def egg(M, T_o=20, T_y=70):
    """ calculates the time to cook a perfect egg """
     
    T_w = 100
    rho = 1.038
    K = 5.4E-3
    c = 3.7

    t = ((M**(2/3.0)*c*rho**(1/3.0))/\
    (K*pi**2*(4*pi/3)**(2/3.0)))*\
    log(0.76*(float(T_o - T_w)/(T_y - T_w)))

    return t

for T_y in 63, 70:
    for M in 47, 67:
        for T_o in 4, 25:
            t = egg(M, T_o, T_y)
            print 'Ty=%d, M=%d, To=%2d, t=%.1f min' % (T_y, M, T_o, t)
