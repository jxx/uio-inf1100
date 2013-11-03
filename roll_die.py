import random

N = 10000
M = 0

for e in range(N):
    r = random.randint(1,6) + random.randint(1,6)
    if r <= 3:
        M += 1
p = float(M)/N

print 'P: %.6f' % p
