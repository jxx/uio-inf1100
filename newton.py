import sys
def newton(f,x, dfdx, epsilon=1e-10, N=100):
    while abs(f(x))>epsilon:
        n = 0
        x = x - f(x)/dfdx(x)
        n += 2
        
        if n > N:
            print "Exceeded max iterations"
            return None, n

    return x, N

def f(x):
    return x**2 - a

def dfdx(x):
    return 2*x

a = float(sys.argv[1])

print newton(f, a, dfdx)
