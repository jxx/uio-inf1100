a = 1/947.0*947
b = 1
if a != b:
    print 'Wrong result using !='

eps = 1e-15

if abs(a-b) > eps:
    print 'Wrong result (with epsilon)'

from scitools.std.float_eq import float_eq


