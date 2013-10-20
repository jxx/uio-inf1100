""" Reads src/funcif/lnsum.txt which contains:

x=10, ln(1+x)=2.3979
n=1    0.909091    (next term: 4.13e-01  error: 1.49e+00)
n=2    1.32231     (next term: 2.50e-01  error: 1.08e+00)
n=10   2.17907     (next term: 3.19e-02  error: 2.19e-01)
n=100  2.39789     (next term: 6.53e-07  error: 6.59e-06)
n=500  2.3979      (next term: 3.65e-24  error: 6.22e-15)

x=100, ln(1+x)=4.61512
n=1    0.990099    (next term: 4.90e-01  error: 3.63e+00)
n=2    1.48025     (next term: 3.24e-01  error: 3.13e+00)
n=10   2.83213     (next term: 8.15e-02  error: 1.78e+00)
n=100  4.39574     (next term: 3.62e-03  error: 2.19e-01)
n=500  4.61395     (next term: 1.37e-05  error: 1.18e-03)

x=1000, ln(1+x)=6.90875
n=1    0.999001    (next term: 4.99e-01  error: 5.91e+00)
n=2    1.498       (next term: 3.32e-01  error: 5.41e+00)
n=10   2.919       (next term: 8.99e-02  error: 3.99e+00)
n=100  5.08989     (next term: 8.95e-03  error: 1.82e+00)
n=500  6.34928     (next term: 1.21e-03  error: 5.59e-01)



epsilon: 1e-04, exact error: 8.18e-04, n=55
epsilon: 1e-06, exact error: 9.02e-06, n=97
epsilon: 1e-08, exact error: 8.70e-08, n=142
epsilon: 1e-10, exact error: 9.20e-10, n=187
epsilon: 1e-12, exact error: 9.31e-12, n=233

and extracts the numbers corresponding to epsilon, exact error, and n.
Stores the numbers in three arrays and plot epsilon and the exact error versus n.
Use a logarithmic scale on the y axis (enabled by the log='y' keyword argument to
the plot function).
"""

from scitools.std import *

# Recycled plot saver
def saveplotpng(filename):
    savefig(filename + '.png')
    print 'Plot saved as ' + filename + '.png'

# File parser
def parse_lnsum(filename):
    f = open(filename, 'r')

    epsilon = []
    exact_error = []
    n = []

    #Ignore all other lines in file.
    for line in f:
        if not line.startswith("epsilon:"):
            continue

        # Parse data
        epsilon.append(float(line[9:14]))
        exact_error.append(float(line[29:37]))
        n.append(int(line[41:]))

    # Assign to arrays
    n_array = array(n)
    epsilon_array = array(epsilon)
    exact_error_array = array(exact_error)
    return n_array, epsilon_array, exact_error_array

# Call mehtod
text = parse_lnsum('src/funcif/lnsum.txt')

# Plot results and save
plot(text[0],text[1],text[0],text[2],
     log='y', xlabel='n',
     legend=('epsilon', 'exact error'))
saveplotpng('6.11_read_error')


"""
$ python 6.11_read_error.py 
Plot saved as 6.11_read_error.png
"""
