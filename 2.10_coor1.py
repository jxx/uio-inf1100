h = 0.01 #step
x = [] #empty list

for i in range(0, 101, 1):
    x_i = 1 + (i * h)
    x.append(x_i)


# print x

for x_i in x:
    print '%.3f' % x_i
