print '------------------'     # table heading
F = 0                          # start value for C
dF  = 10                         # increment of C in loop
while F <= 100:                 # loop heading with condition
    C = (5/9.0) * (F - 32)         # 1st statement inside loop
    print '%8.0f %8.1f' % (F,C) # 2nd statement inside loop
    F = F + dF                 # 3rd statement inside loop
print '------------------'     # end of table line (after loop)
