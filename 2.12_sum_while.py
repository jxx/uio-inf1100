""" Broken code for harmonic series. Fix it.
s = 0; k = 1; M = 100
while k < M:
    s += 1/k
print s
"""

# 1) add k counter to avoid infinite loop
# 2) make loop start at 1 and stop at 100: use <= instead of <
# 3) k and s must be floats to calculate correct sum

s = 0.; k = 1.; M = 100

while k <= M:
    s += 1/k 
    k += 1
print s 

"""
$ python 2.12_sum_while.py 
5.18737751764
"""
