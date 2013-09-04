# Broken code. Fix it.
# s = 0; k = 1; M = 100
# while k < M:
#    s += 1/k
# print s

s = 0.; k = 01.; M = 100 
# needs s counter to avoid infinite loop
# k, s should be floats to calculate correctly
# k needs to start at 0 for loop to execute properly
while k < M:
    k += 1 # added counter.
    s += 1/k 
print s 
