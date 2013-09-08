def roots(a, b, c):
    from numpy.lib.scimath import sqrt
    r1 = (-b + sqrt(b**2 - 4*a*c))/(2*a)
    r2 = (-b - sqrt(b**2 - 4*a*c))/(2*a)
    return r1, r2

test1 = roots(1, 2, 100)
for item in test1:
    print item, type(item)

test2 = roots(1, 4, 1)
for item in test2:
    print item, type(item)
