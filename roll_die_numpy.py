import numpy as np

N = 100000000
M = 0

result = np.random.randint(1, 7, size = N)

sixes = np.sum(result == 6)

print 'P: %.6f' % (float(sixes)/N)
