from math import sqrt, pi, exp

m = 0.
s = 2.
x = 1.

gaussian = ( 1 / sqrt( 2 * pi ) * s  ) * exp( ( -1./2.  * ( (x-m) / s) ** 2 ) ) 

print gaussian

