print "8.01 flip a coin"

import random, sys

N = int(sys.argv[1])
heads = 0
two_heads = 0

nheads = 0
n = 5

for e in range(N):
    rr = [random.random() for i in range(n)]
    all_heads = True
    for r_i in rr:
        if r_i <= 0.5:
            all_heads = False            
 #           heads += 1
    if all_heads:
        nheads += 1
#    r2 = random.random()

#    if r <= .5 and r2 <= .5:
#        two_heads += 1

    
#print 'Number of heads:', heads

#Probability
#print 'p: %.4f' % (heads/float(N))
#r = random.random() # 0,10

#print 'two heads:', two_heads
#print 'p: %.4f' % (two_heads/float(N))

print 'n:', n
print 'All heads:', nheads


